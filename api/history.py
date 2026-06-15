from fastapi import APIRouter

from database.db import SessionLocal
from database.crud import get_all_reports

router = APIRouter(
    prefix="/history",
    tags=["History"]
)


@router.get("/")
def history():

    db = SessionLocal()

    reports = get_all_reports(db)

    db.close()

    return reports