from sqlalchemy.orm import Session
from app.models.resume import Resume

class ResumeDatabaseService:

    @staticmethod
    def create_resume(db: Session,
                      candidate_name: str,
                      filename: str,) -> Resume:

        resume = Resume(
            candidate_name=candidate_name,
            filename=filename,
            text="")

        db.add(resume)
        db.commit()
        db.refresh(resume)
        return resume

    @staticmethod
    def update_resume_text(\
        db: Session,
        resume_id: int,
        text: str):

        resume=(db.query(Resume).filter(Resume.id == resume_id).first())
        if resume:
            resume.text = text
            db.commit()
            
            return resume