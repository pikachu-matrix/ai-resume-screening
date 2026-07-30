"""
Routing the APIS related to Job Services 
Response posting 
"""
from fastapi import APIRouter

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
):
    return JobService.create_job(job)