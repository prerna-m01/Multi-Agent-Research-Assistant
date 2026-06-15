from database.models import Research


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
        .order_by(Research.id.desc())
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

    return report

