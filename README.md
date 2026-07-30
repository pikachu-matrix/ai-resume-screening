# ai-resume-screening
AI-powered Resume Screening and Candidate Ranking System using FastAPI, React, RAG, LLMs, Vector Database, and Docker.

# AI Resume Screening & Candidate Ranking System

An AI-powered recruitment platform that helps recruiters screen, compare, and rank multiple candidates against a single Job Description (JD). The system uses Resume Parsing, Retrieval-Augmented Generation (RAG), Vector Search, and Large Language Models (LLMs) to provide intelligent candidate matching with transparent explanations.

---

## Overview

Hiring teams often spend hours manually reviewing resumes for a single job opening. This project automates much of that process by extracting candidate information, understanding job requirements, comparing resumes semantically, and generating explainable rankings.

The application is designed as a production-style full-stack AI system that demonstrates modern software engineering practices, scalable architecture, and Generative AI integration.

---

## Features

- Upload a single Job Description
- Upload multiple resumes (PDF/DOCX)
- Automatic resume parsing
- Candidate information extraction
- Semantic similarity using embeddings
- Vector database storage
- Retrieval-Augmented Generation (RAG)
- AI-powered resume analysis
- Candidate ranking
- Skill gap analysis
- Experience comparison
- Education comparison
- Recruiter dashboard
- PDF/CSV report generation
- Authentication & user management
- Dockerized deployment
- Cloud-ready architecture

---

# System Workflow

```

Recruiter
│
├── Upload Job Description
│
├── Upload Multiple Resumes
│
▼

Resume Parsing
│
▼

Text Preprocessing
│
▼

Embedding Generation
│
▼

Vector Database
│
▼

RAG Retrieval
│
▼

LLM Analysis
│
▼

Candidate Ranking
│
▼

Recruiter Dashboard

```

---

# Tech Stack

## Backend

- Python
- FastAPI
- SQLAlchemy
- Pydantic

## Frontend

- React
- HTML
- CSS
- JavaScript

## AI & NLP

- OpenAI GPT
- Azure OpenAI
- Prompt Engineering
- Sentence Transformers
- BGE Embeddings

## RAG

- LangChain
- LlamaIndex

## Vector Database

- ChromaDB
- FAISS

## Database

- PostgreSQL
- SQLite (Development)

## Resume Parsing

- PyMuPDF
- pdfplumber
- python-docx

## Deployment

- Docker
- Docker Compose
- Kubernetes
- Azure / AWS

---

# Project Architecture

```

Frontend (React)
│

REST API

│
Backend (FastAPI)
│
├── Authentication
├── Resume Upload
├── Job Description API
├── Resume Parser
├── Text Processing
├── Embedding Service
├── Vector Search
├── RAG Pipeline
├── LLM Service
├── Ranking Engine
└── Report Generator

│

PostgreSQL

ChromaDB

OpenAI API

```

---

# Project Structure

```

ai-resume-screening/

├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── auth/
│   │   ├── parser/
│   │   ├── preprocessing/
│   │   ├── embeddings/
│   │   ├── rag/
│   │   ├── ranking/
│   │   ├── database/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── utils/
│   │   └── main.py
│   │
│   ├── tests/
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/
│
├── database/
│
├── docker/
│
├── kubernetes/
│
├── docs/
│
├── README.md
│
└── .gitignore

```

---

# Core Components

- Authentication
- Resume Upload
- Job Description Management
- Resume Parsing
- Text Cleaning
- Candidate Information Extraction
- Embedding Generator
- Vector Database
- RAG Retrieval
- LLM Analysis
- Candidate Ranking
- Dashboard
- Report Export

---

# AI Pipeline

```

Resume
│
▼

Extract Text
│
▼

Clean Text
│
▼

Generate Embeddings
│
▼

Store in ChromaDB
│
▼

Retrieve Relevant Sections
│
▼

LLM Comparison
│
▼

Generate Match Score
│
▼

Rank Candidates

```

---

# Candidate Evaluation

Each candidate is evaluated based on:

- Technical Skills
- Soft Skills
- Work Experience
- Education
- Certifications
- Project Relevance
- Semantic Similarity
- Overall Job Fit

The system provides explainable results instead of simply assigning a score.

---

# Security & Responsible AI

The application is designed to assist recruiters and not replace human decision-making.

The system intentionally ignores sensitive personal attributes such as:

- Age
- Gender
- Religion
- Nationality
- Marital Status
- Photograph

Candidate rankings are based only on job-related qualifications and experience.

---

# Learning Objectives

This project demonstrates practical implementation of:

- Python
- FastAPI
- REST APIs
- React
- SQL
- PostgreSQL
- Docker
- Kubernetes
- Git & GitHub
- Prompt Engineering
- Retrieval-Augmented Generation (RAG)
- Embeddings
- Vector Databases
- Resume Parsing
- LLM Integration
- Cloud Deployment

---

# Future Improvements

- Multi-language resume support
- OCR for scanned resumes
- Interview question generation
- Candidate chat assistant
- Recruiter analytics dashboard
- Email integration
- Calendar scheduling
- ATS integration
- Resume recommendations
- Fine-tuned domain-specific models

---

# Development Roadmap

### Phase 1

- Backend Setup
- FastAPI
- Resume Upload API

### Phase 2

- Resume Parsing
- Text Extraction
- Preprocessing

### Phase 3

- LLM Integration
- Prompt Engineering
- Resume vs JD Comparison

### Phase 4

- Embeddings
- ChromaDB
- RAG Pipeline

### Phase 5

- Ranking Engine
- Dashboard
- Reports

### Phase 6

- Docker
- Kubernetes
- Cloud Deployment

---

# Getting Started

### Clone the Repository

```bash
git clone https://github.com/<pikachu-matrix>/ai-resume-screening.git
```

### Navigate to the Project

```bash
cd ai-resume-screening
```

### Backend Setup

```bash
cd backend

python -m venv venv

# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

### Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

---

# Project Status

🚧 Currently under active development.

The project is being built incrementally with production-ready architecture, modern AI techniques, and scalable deployment practices.

---

# License

This project is intended for educational, research, and portfolio purposes.

---

## Author

Engineering Researcher | AI Engineer | Generative AI | RAG | FastAPI | React | Python

---

## Acknowledgements

Special thanks to the open-source community and the developers of FastAPI, React, LangChain, ChromaDB, PostgreSQL, Docker, and OpenAI for providing the tools that make this project possible.

