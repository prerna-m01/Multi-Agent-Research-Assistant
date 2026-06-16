from pydantic import BaseModel


class ResearchRequest(
    BaseModel
):

    query: str

    model_config = {
        "json_schema_extra": {
            "example": {
                "query":
                "Impact of AI on Healthcare"
            }
        }
    }