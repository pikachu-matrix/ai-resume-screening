from pydantic import BaseModel, Field

class JobDescriptionRequest(BaseModel):
    job_title: str = Field(..., min_length=3, max_length=100)
    company_name: str = Field(..., min_length=2, max_length=100)
    job_description: str = Field(..., min_length=20)

class JobDescriptionResponse(BaseModel):
    message: str
    job_title: str
    company_name: str