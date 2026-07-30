from fastapi import FastAPI
from app.api.health import health_router
from app.api.jobs import job_router
from app.api.resumes import resume_router



application=FastAPI(
title="AI Resume Screenning API",
description="Backend API for Resume Screening and Candidate Ranking.",
version="1.0.0"
)
application.include_router(health_router)
application.include_router(job_router)
application.include_router(resume_router)




@application.get("/")
def read_home():
    return {
    "message": "Welcome to thr AI Resume Screening API."
        }

