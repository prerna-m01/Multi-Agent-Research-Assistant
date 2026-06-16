from fastapi import APIRouter
from fastapi.responses import FileResponse

from database.db import SessionLocal
from database.crud import (
    get_report_by_id
)

router = APIRouter(
    prefix="/report",
    tags=["Reports"]
)


@router.get(
    "/{report_id}/download"
)
def download_report(
    report_id: int
):

    db = SessionLocal()

    report = get_report_by_id(
        db,
        report_id
    )

    db.close()

    if not report:

        return {
            "error":
            "Report not found"
        }

    filename = (
        f"report_{report_id}.txt"
    )

    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(
            report.report
        )

    return FileResponse(
        filename,
        media_type="text/plain",
        filename=filename
    )