from sqlalchemy import Column, Integer, String, Text
from database.db import Base


class Research(Base):
    __tablename__ = "research_reports"

    id = Column(Integer, primary_key=True, index=True)

    query = Column(String, nullable=False)

    report = Column(Text, nullable=False)