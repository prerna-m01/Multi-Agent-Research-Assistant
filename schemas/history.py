from pydantic import BaseModel
from datetime import datetime


class HistoryResponse(BaseModel):

    id: int

    query: str

    report: str

    created_at: datetime

    class Config:
        from_attributes = True

model_config = {
    "json_schema_extra": {
        "example": {
            "id": 1,
            "query": "AI",
            "report": "..."
        }
    }
}