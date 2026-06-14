from pydantic import BaseModel
from typing import List, Dict


class SearchResponse(BaseModel):
    query: str
    results: List[Dict]