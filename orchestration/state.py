from typing import TypedDict, List


class ResearchState(TypedDict):
    query: str
    plan: List[str]
    search_results: List[dict]
    summary: str
    final_report: str