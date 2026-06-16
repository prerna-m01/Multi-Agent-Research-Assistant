from fastapi import APIRouter, HTTPException

from database.db import SessionLocal

from database.crud import (
    get_documents,
    get_document_by_id,
    delete_document
)

router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)


@router.get("/")
def list_documents():

    db = SessionLocal()

    try:

        return get_documents(db)

    finally:

        db.close()


@router.get("/{document_id}")
def get_document(
    document_id: int
):

    db = SessionLocal()

    try:

        document = get_document_by_id(
            db,
            document_id
        )

        if not document:

            raise HTTPException(
                status_code=404,
                detail="Document not found"
            )

        return document

    finally:

        db.close()


@router.delete("/{document_id}")
def remove_document(
    document_id: int
):

    db = SessionLocal()

    try:

        result = delete_document(
            db,
            document_id
        )

        if not result:

            raise HTTPException(
                status_code=404,
                detail="Document not found"
            )

        return {
            "success": True,
            "message": "Document deleted",
            "document_id": document_id
        }

    finally:

        db.close()