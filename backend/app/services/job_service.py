from app.schemas.job import (
    JobDescriptionRequest,
    JobDescriptionResponse,
)


class JobService:

    @staticmethod #related to class, does not need object data or class data
    def create_job(
        job: JobDescriptionRequest, #parameter name - job, expected type - job description request
    ) -> JobDescriptionResponse: # job description response

        return JobDescriptionResponse(
            message="Job Description received successfully.",
            job_title=job.job_title,
            company_name=job.company_name,
        )