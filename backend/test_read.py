from app.database import SessionLocal
from app.models.job import Job

# Open database session
db = SessionLocal()

# Fetch all jobs
jobs = db.query(Job).all()

# Print jobs
for job in jobs:
    print("-" * 50)
    print(f"ID          : {job.id}")
    print(f"Job Title   : {job.job_title}")
    print(f"Company     : {job.company_name}")
    print(f"Description : {job.job_description}")

# Close session
db.close()
