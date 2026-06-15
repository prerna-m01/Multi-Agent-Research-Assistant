from pydantic import BaseModel


class ResearchStatusResponse(
    BaseModel
):

    id: int

    status: str