from fastapi import APIRouter

from schemas.request import ResearchRequest
from schemas.response import ResearchResponse

from agents.planner_agent import PlannerAgent
from agents.search_agent import SearchAgent
from orchestration.workflow import ResearchWorkflow

workflow = ResearchWorkflow()

search_agent = SearchAgent()

router = APIRouter(
    prefix="/research",
    tags=["Research"]
)

planner = PlannerAgent()


@router.post("/", response_model=ResearchResponse)
def research(request: ResearchRequest):

    plan = planner.create_plan(request.query)

    return ResearchResponse(
        query=request.query,
        research_plan=plan
    )

@router.post("/search")
def search(request: ResearchRequest):

    results = search_agent.search(
        request.query
    )

    return {
        "query": request.query,
        "results": results
    }

@router.post("/")
def research(request: ResearchRequest):

    result = workflow.run(request.query)

    return result