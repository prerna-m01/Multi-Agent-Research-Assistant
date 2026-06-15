from fastapi import APIRouter
from fastapi import HTTPException

from schemas.request import ResearchRequest

from orchestration.workflow import ResearchWorkflow

from database.db import SessionLocal

from database.crud import (
    create_research_job,
    get_report_by_id
)

from core.logger import logger

router = APIRouter(
    prefix="/research",
    tags=["Research"]
)

workflow = ResearchWorkflow()


@router.post("/")
async def research(
    request: ResearchRequest
):

    db = SessionLocal()

    try:

        job = create_research_job(
            db,
            request.query
        )

        logger.info(
            f"Research job created: {job.id}"
        )

        await workflow.run(
            request.query,
            job.id
        )

        return {
            "job_id": job.id,
            "status": "completed"
        }

    except Exception as e:

        logger.exception(
            "Research failed"
        )

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

    finally:
        db.close()


@router.get("/{job_id}/status")
def get_status(
    job_id: int
):

    db = SessionLocal()

    report = get_report_by_id(
        db,
        job_id
    )

    db.close()

    if not report:

        raise HTTPException(
            status_code=404,
            detail="Job not found"
        )

    return {
        "id": report.id,
        "status": report.status
    }