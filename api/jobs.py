from fastapi import APIRouter

from database.db import SessionLocal
from database.models import Research

router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"]
)


@router.get("/{job_id}")
def get_job(job_id: int):

    db = SessionLocal()

    try:

        job = (
            db.query(Research)
            .filter(
                Research.id == job_id
            )
            .first()
        )

        if not job:

            return {
                "error":
                "Job not found"
            }

        return {
            "id": job.id,
            "query": job.query,
            "status": job.status
        }

    finally:

        db.close()