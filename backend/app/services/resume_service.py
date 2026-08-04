from pathlib import Path

from fastapi import UploadFile

from app.services.parser import ParserService


class ResumeService:

    UPLOAD_FOLDER = Path("uploads")

    @staticmethod
    async def upload_resumes(
        resumes: list[UploadFile],
    ):

        ResumeService.UPLOAD_FOLDER.mkdir(exist_ok=True)

        uploaded_files = []

        for resume in resumes:

            file_path = ResumeService.UPLOAD_FOLDER / resume.filename

            with open(file_path, "wb") as file:
                file.write(await resume.read())

            extracted_text = ParserService.extract_text(
                str(file_path)
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