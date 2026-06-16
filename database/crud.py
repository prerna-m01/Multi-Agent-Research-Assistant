from database.models import (
    Research,
    UploadedDocument
)


# ==========================
# Research CRUD
# ==========================

def save_research(
    db,
    query,
    report
):

    research = Research(
        query=query,
        report=report
    )

    db.add(research)

    db.commit()

    db.refresh(research)

    return research


def get_all_reports(db):

    return (
        db.query(Research)
        .order_by(
            Research.id.desc()
        )
        .all()
    )


def get_report_by_id(
    db,
    report_id
):

    return (
        db.query(Research)
        .filter(
            Research.id == report_id
        )
        .first()
    )


def delete_report(
    db,
    report_id
):

    report = (
        db.query(Research)
        .filter(
            Research.id == report_id
        )
        .first()
    )

    if report:

        db.delete(report)

        db.commit()

    return report


# ==========================
# Research Jobs
# ==========================

def create_research_job(
    db,
    query
):

    research = Research(
        query=query,
        status="pending"
    )

    db.add(research)

    db.commit()

    db.refresh(research)

    return research


def update_status(
    db,
    report_id,
    status
):

    report = (
        db.query(Research)
        .filter(
            Research.id == report_id
        )
        .first()
    )

    if report:

        report.status = status

        db.commit()

        db.refresh(report)

    return report


def update_report(
    db,
    report_id,
    final_report
):

    report = (
        db.query(Research)
        .filter(
            Research.id == report_id
        )
        .first()
    )

    if report:

        report.report = final_report

        report.status = "completed"

        db.commit()

        db.refresh(report)

    return report


# ==========================
# Documents CRUD
# ==========================

def save_document(
    db,
    filename
):

    doc = UploadedDocument(
        filename=filename
    )

    db.add(doc)

    db.commit()

    db.refresh(doc)

    return doc


def get_documents(
    db
):

    return (
        db.query(UploadedDocument)
        .order_by(
            UploadedDocument.id.desc()
        )
        .all()
    )


def get_document_by_id(
    db,
    document_id
):

    return (
        db.query(UploadedDocument)
        .filter(
            UploadedDocument.id == document_id
        )
        .first()
    )


def delete_document(
    db,
    document_id
):

    doc = (
        db.query(UploadedDocument)
        .filter(
            UploadedDocument.id == document_id
        )
        .first()
    )

    if doc:

        db.delete(doc)

        db.commit()

    return doc

def delete_document(
    db,
    document_id
):

    doc = db.query(
        Document
    ).filter(
        Document.id == document_id
    ).first()

    if doc:

        db.delete(doc)

        db.commit()

    return doc