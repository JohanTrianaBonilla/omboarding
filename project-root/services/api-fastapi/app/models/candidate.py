from sqlalchemy import Column, Integer, String, Text
from app.core.database import Base

class Candidate(Base):
    __tablename__ = "candidates"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    skills = Column(Text, nullable=True)
    experience = Column(Text, nullable=True)
