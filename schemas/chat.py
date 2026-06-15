from pydantic import BaseModel
from typing import List

class ChatRequest(BaseModel):
    question: str

class SourceResponse(
    BaseModel
):
    page: int
    source: str
    score: float

class ChatResponse(
    BaseModel
):
    answer: str
    sources: List[SourceResponse]