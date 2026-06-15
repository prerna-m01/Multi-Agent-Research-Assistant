from fastapi import APIRouter

from schemas.chat import ChatRequest

from services.rag_service import answer_question

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


@router.post("/")
def chat(
    request: ChatRequest
):

    result = answer_question(
        request.question
    )

    return result