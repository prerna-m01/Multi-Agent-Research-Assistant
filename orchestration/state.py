from typing import TypedDict, List, Dict


class ResearchState(TypedDict):
    query: str
    plan: List[str]
    search_results: List[Dict]
    summary: str
    final_report: str