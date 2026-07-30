from typing import Annotated

from fastapi import APIRouter, File, UploadFile

from app.services.resume_service import ResumeService

from app.schemas.resume import ResumeUploadResponse

resume_router = APIRouter(
    prefix="/resumes",
    tags=["Resumes"],
)

@resume_router.post(
    "/upload",
    response_model=ResumeUploadResponse,
)
async def upload_resumes(
    resumes: Annotated[list[UploadFile], File(...)],
):
    return await ResumeService.upload_resumes(resumes)