from pathlib import Path

from fastapi import UploadFile

from app.services.parser import ParserService
from sqlalchemy.orm import Session
from app.services.resume_database_service import ResumeDatabaseService


class ResumeService:

    UPLOAD_FOLDER = Path("uploads")

    @staticmethod
    async def upload_resumes(
        resumes: list[UploadFile], db:Session,
    ):

        ResumeService.UPLOAD_FOLDER.mkdir(exist_ok=True)

        uploaded_files = []

        for resume in resumes:

            file_path = ResumeService.UPLOAD_FOLDER / resume.filename

            with open(file_path, "wb") as file:
                file.write(await resume.read())

            resume_record = ResumeDatabaseService.create_resume(
                db=db,
                candidate_name=file_path.stem,
                filename=resume.filename,
            )

            extracted_text = ParserService.extract_text(
                str(file_path)
            )
            ResumeDatabaseService.update_resume_text(
                db=db,
                resume_id=resume_record.id,
                text=extracted_text,
            )

            uploaded_files.append(
                {
                    "filename": resume.filename,
                    "content_type": resume.content_type,
                    "characters": len(extracted_text),
                    "preview": extracted_text[:300],
                }
            )

        return {
            "message": "Resume processed successfully.",
            "total_files": len(uploaded_files),
            "files": uploaded_files,
        }