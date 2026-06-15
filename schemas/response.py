from pydantic import BaseModel
from typing import List, Dict


class ResearchResponse(BaseModel):
    query: str
    plan: List[str]
    search_results: List[Dict]
    summary: str
    final_report: str