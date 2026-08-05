"""
Routing the APIs related to Job Services
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database_session import get_db
from app.schemas.job import (
    JobDescriptionRequest,
    JobDescriptionResponse,
)
from app.services.job_service import JobService

job_router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"],
)


@job_router.post(
    "",
    response_model=JobDescriptionResponse,
)
def create_job(
    job: JobDescriptionRequest,
    db: Session = Depends(get_db),
):
    return JobService.create_job(job, db)