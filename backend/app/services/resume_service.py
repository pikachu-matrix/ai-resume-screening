from fastapi import UploadFile


class ResumeService:

    @staticmethod
    async def upload_resumes(
        resumes: list[UploadFile],
    ):
        uploaded_files = []

        for resume in resumes:
            uploaded_files.append(
                {
                    "filename": resume.filename,
                    "content_type": resume.content_type,
                }
            )

        return {
            "message": "Resumes uploaded successfully.",
            "total_files": len(uploaded_files),
            "files": uploaded_files,
        }