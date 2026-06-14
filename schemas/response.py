from pydantic import BaseModel
from typing import List


class ResearchPlan(BaseModel):
    steps: List[str]


class ResearchResponse(BaseModel):
    query: str
    research_plan: List[str]