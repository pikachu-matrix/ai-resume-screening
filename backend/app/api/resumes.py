from typing import Annotated

from fastapi import APIRouter, File, UploadFile, Depends

from sqlalchemy.orm import Session

from app.database_session import get_db

from app.services.resume_service import ResumeService
#from app.schemas.resume import ResumeUploadResponse

resume_router = APIRouter(
    prefix="/resumes",
    tags=["Resumes"],
)

@resume_router.post(
    "/upload",
)
async def upload_resumes(
    resumes: Annotated[list[UploadFile], File(...)],
    db: Session = Depends(get_db),
):
    return await ResumeService.upload_resumes(resumes, db)