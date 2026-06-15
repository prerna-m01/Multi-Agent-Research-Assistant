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

    return db.query(
        Research
    ).all()