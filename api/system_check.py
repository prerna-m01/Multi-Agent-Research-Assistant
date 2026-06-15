from fastapi import APIRouter
from sqlalchemy import text

from database.db import SessionLocal

from services.rag_service import (
    embedding_model
)

from services.llm_service import (
    LLMService
)

from services.tavily_service import (
    TavilyService
)

from langchain_community.vectorstores import (
    Chroma
)

router = APIRouter(
    prefix="/system-check",
    tags=["System Check"]
)


@router.get("/")
def system_check():

    results = {}

    # Database Check
    try:

        db = SessionLocal()

        db.execute(
            text("SELECT 1")
        )

        results["database"] = "OK"

        db.close()

    except Exception as e:

        results["database"] = (
            f"FAILED: {str(e)}"
        )

    # Vector Store Check
    try:

        Chroma(
            persist_directory="vectorstore",
            embedding_function=embedding_model
        )

        results["vectorstore"] = "OK"

    except Exception as e:

        results["vectorstore"] = (
            f"FAILED: {str(e)}"
        )

    # Gemini Check
    try:

        llm = LLMService()

        response = llm.generate(
            "Reply with exactly: OK"
        )

        if response:

            results["gemini"] = "OK"

        else:

            results["gemini"] = "FAILED"

    except Exception as e:

        results["gemini"] = (
            f"FAILED: {str(e)}"
        )

    # Tavily Check
    try:

        tavily = TavilyService()

        tavily.search(
            "Artificial Intelligence"
        )

        results["tavily"] = "OK"

    except Exception as e:

        results["tavily"] = (
            f"FAILED: {str(e)}"
        )

    return {
        "success": True,
        "checks": results
    }