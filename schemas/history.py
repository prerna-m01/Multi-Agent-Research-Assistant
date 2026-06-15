from pydantic import BaseModel


class HistoryResponse(BaseModel):

    id: int

    query: str

    report: str

    class Config:
        from_attributes = True