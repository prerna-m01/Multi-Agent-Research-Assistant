from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime
)

from datetime import datetime

from database.db import Base


class Research(Base):

    __tablename__ = "research_reports"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    query = Column(
        String,
        nullable=False
    )

    report = Column(
        Text,
        nullable=True
    )

    status = Column(
        String,
        default="pending"
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

class UploadedDocument(Base):

    __tablename__ = "documents"

    id = Column(
        Integer,
        primary_key=True
    )

    filename = Column(
        String,
        nullable=False
    )

    upload_time = Column(
        DateTime,
        default=datetime.utcnow
    )