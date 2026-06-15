from fastapi import APIRouter

from database.db import SessionLocal
from database.models import Research

router = APIRouter(
    prefix="/stats",
    tags=["Stats"]
)


@router.get("/")
def get_stats():

    db = SessionLocal()

    try:

        report_count = db.query(
            Research
        ).count()

        return {
            "research_reports":
            report_count,

            "database":
            "healthy"
        }

    finally:
        db.close()