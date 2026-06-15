from fastapi import APIRouter

from schemas.request import ResearchRequest

from agents.search_agent import SearchAgent
from orchestration.workflow import ResearchWorkflow

router = APIRouter(
    prefix="/research",
    tags=["Research"]
)

workflow = ResearchWorkflow()
search_agent = SearchAgent()


@router.post("/")
def research(request: ResearchRequest):

    result = workflow.run(
        request.query
    )

    return result


@router.post("/search")
def search(request: ResearchRequest):

    results = search_agent.search(
        request.query
    )

    return {
        "query": request.query,
        "results": results
    }