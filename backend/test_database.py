from app.database import SessionLocal
from app.models.job import Job

#Create a database session
db = SessionLocal()

#Create a new job object
new_job = Job(
    job_title="AI Engineer",
    company_name="Kanerika",
    job_description="Looking for an AI Engineer with Python, FastAPI, SQL, Machine Learning and GenAI skills."
)
#Add the object to the session
db.add(new_job)

#save changes to PostgreSQL
db.commit()

#close the session
db.close()

print("Job inserted successfully!")