from pydantic import BaseModel
from typing import List, Dict, Any


class ResearchData(BaseModel):
    query: str
    plan: List[str]
    search_results: List[Dict]
    summary: str
    final_report: str


class ResearchResponse(BaseModel):
    success: bool
    message: str
    data: ResearchData