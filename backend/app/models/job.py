from sqlalchemy import Column, Integer, String, Text
from app.database import Base

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    job_title = Column(String(100), nullable=False)
    company_name = Column(String(100), nullable=False)
    job_description = Column(Text, nullable=False)