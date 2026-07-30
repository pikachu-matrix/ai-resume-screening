from pydantic import BaseModel


class UploadedFile(BaseModel):
    filename: str
    content_type: str


class ResumeUploadResponse(BaseModel):
    message: str
    total_files: int
    files: list[UploadedFile]