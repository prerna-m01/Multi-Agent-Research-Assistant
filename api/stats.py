from fastapi import APIRouter
from sqlalchemy import func

from database.db import SessionLocal
from database.models import (
    Research,
    UploadedDocument
)

router = APIRouter(
    prefix="/stats",
    tags=["Stats"]
)


@router.get("/")
def stats():

    db = SessionLocal()

    try:

        report_count = (
            db.query(
                func.count(
                    Research.id
                )
            )
            .scalar()
        )

        document_count = (
            db.query(
                func.count(
                    UploadedDocument.id
                )
            )
            .scalar()
        )

        return {
            "research_reports":
            report_count,

            "uploaded_documents":
            document_count,

            "database":
            "healthy",

            "vectorstore":
            "healthy"
        }

    finally:

        db.close()