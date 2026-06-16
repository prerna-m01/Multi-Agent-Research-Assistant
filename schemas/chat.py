from pydantic import BaseModel
from typing import List


class ChatRequest(BaseModel):

    question: str


class SourceResponse(
    BaseModel
):

    page: int | str

    source: str

    score: float


class ChatResponse(
    BaseModel
):

    answer: str

    sources: List[
        SourceResponse
    ]

model_config = {
    "json_schema_extra": {
        "example": {
            "question":
            "Summarize the uploaded PDF"
        }
    }
}