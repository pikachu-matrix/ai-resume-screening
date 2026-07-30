from fastapi import FastAPI
from app.api.health import health_router


application=FastAPI(
title="AI Resume Screenning API",
description="Backend API for Resume Screening and Candidate Ranking.",
version="1.0.0"
)
application.include_router(health_router)

@application.get("/")
def read_home():
    return {
    "message": "Welcome to thr AI Resume Screening API."
        }