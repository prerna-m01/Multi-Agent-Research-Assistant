from fastapi import APIRouter

from schemas.request import ResearchRequest
from schemas.response import ResearchResponse

from orchestration.workflow import ResearchWorkflow

router = APIRouter(
    prefix="/research",
    tags=["Research"]
)

workflow = ResearchWorkflow()


@router.post(
    "/",
    response_model=ResearchResponse
)
def research(request: ResearchRequest):

    result = workflow.run(
        request.query
    )

    return ResearchResponse(
        query=result["query"],
        plan=result["plan"],
        search_results=result["search_results"],
        summary=result["summary"],
        final_report=result["final_report"]
    )