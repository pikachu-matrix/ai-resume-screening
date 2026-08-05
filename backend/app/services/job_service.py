from sqlalchemy.orm import Session

from app.models.job import Job
from app.schemas.job import (
    JobDescriptionRequest,
    JobDescriptionResponse,
)


class JobService:

    @staticmethod
    def create_job(
        job: JobDescriptionRequest,
        db: Session,
    ) -> JobDescriptionResponse:

        new_job = Job(
            job_title=job.job_title,
            company_name=job.company_name,
            job_description=job.job_description,
        )

        db.add(new_job)
        db.commit()
        db.refresh(new_job)

        return JobDescriptionResponse(
            message="Job Description received successfully.",
            job_title=new_job.job_title,
            company_name=new_job.company_name,
        )