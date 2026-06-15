from pydantic import BaseModel
from datetime import datetime


class HistoryResponse(BaseModel):

    id: int

    query: str

    report: str

    created_at: datetime

    class Config:
        from_attributes = True