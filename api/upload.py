from fastapi import (
    APIRouter,
    UploadFile,
    File
)

import shutil
import os

from services.rag_service import (
    process_pdf
)

router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)


@router.post("/")
async def upload_file(
    file: UploadFile = File(...)
):

    os.makedirs(
        "uploads",
        exist_ok=True
    )

    file_path = (
        f"uploads/{file.filename}"
    )

    with open(
        file_path,
        "wb"
    ) as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    process_pdf(
        file_path
    )

    return {
        "message":
        "Document uploaded successfully"
    }