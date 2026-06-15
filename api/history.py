from fastapi import APIRouter, HTTPException

from database.db import SessionLocal

from database.crud import (
    get_all_reports,
    get_report_by_id,
    delete_report
)

router = APIRouter(
    prefix="/history",
    tags=["History"]
)


@router.get("/")
def history():

    db = SessionLocal()

    try:
        return get_all_reports(db)

    finally:
        db.close()


@router.get("/{report_id}")
def history_by_id(
    report_id: int
):
    db = SessionLocal()

    report = get_report_by_id(
        db,
        report_id
    )

    db.close()

    if not report:
        raise HTTPException(
            status_code=404,
            detail="Report not found"
        )

    return report


@router.delete("/{report_id}")
def remove_history(
    report_id: int
):
    db = SessionLocal()

    report = delete_report(
        db,
        report_id
    )

    db.close()

    if not report:
        raise HTTPException(
            status_code=404,
            detail="Report not found"
        )

    return {
        "message":
        "Report deleted successfully"
    }