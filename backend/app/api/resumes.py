from fastapi import APIRouter, File, UploadFile

from app.services.resume_service import ResumeService

resume_router = APIRouter(
    prefix="/resumes",
    tags=["Resumes"],
)


@resume_router.post("/upload")
async def upload_resumes(
    resumes: list[UploadFile] = File(...),
):
    return await ResumeService.upload_resumes(resumes)