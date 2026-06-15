import os

from fastapi import APIRouter
from fastapi import HTTPException
from fastapi.responses import FileResponse

from database.db import SessionLocal
from database.crud import get_report_by_id

from services.pdf_service import generate_pdf
from services.docx_service import generate_docx


router = APIRouter(
    prefix="/export",
    tags=["Export"]
)

@router.get(
    "/pdf/{report_id}"
)
def export_pdf(
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

    os.makedirs(
        "exports/pdf",
        exist_ok=True
    )

    filename = (
        f"exports/pdf/"
        f"report_{report_id}.pdf"
    )

    generate_pdf(
        filename,
        report.query,
        report.report
    )

    return FileResponse(
        filename,
        media_type="application/pdf",
        filename=f"report_{report_id}.pdf"
    )

@router.get(
    "/docx/{report_id}"
)
def export_docx(
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

    os.makedirs(
        "exports/docx",
        exist_ok=True
    )

    filename = (
        f"exports/docx/"
        f"report_{report_id}.docx"
    )

    generate_docx(
        filename,
        report.query,
        report.report
    )

    return FileResponse(
        filename,
        media_type=(
            "application/vnd.openxmlformats-officedocument"
            ".wordprocessingml.document"
        ),
        filename=f"report_{report_id}.docx"
    )