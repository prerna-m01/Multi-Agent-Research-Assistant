from fastapi import APIRouter
from sqlalchemy import func

from database.db import SessionLocal
from database.models import Research

router = APIRouter(
    prefix="/stats",
    tags=["Stats"]
)


@router.get("/")
def stats():

    db = SessionLocal()

    try:

        report_count = db.query(
            func.count(Research.id)
        ).scalar()

        return {
            "research_reports":
            report_count,

            "database":
            "healthy"
        }

    finally:

        db.close()