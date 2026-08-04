# AI Resume Screening System

An end-to-end AI-powered Resume Screening System that automatically processes resumes, extracts text, generates semantic embeddings, and ranks candidates based on their similarity to a job description.

This project is being built step by step using production-style software engineering practices with FastAPI, FAISS, Sentence Transformers, and PostgreSQL.

---

# Current Progress

**Project Completion:** 45%

## Completed Modules

- FastAPI Backend
- Modular Project Architecture
- Job Description API
- Resume Upload API
- Resume Parser (PDF & DOCX)
- Text Cleaning
- Text Chunking
- Sentence Embeddings
- FAISS Vector Search
- Metadata Storage
- Candidate Ranking Engine (Chunk Level)

---

# System Architecture

```
Resume Upload
      │
      ▼
Resume Parser
      │
      ▼
Text Cleaner
      │
      ▼
Text Chunking
      │
      ▼
Sentence Embeddings
      │
      ▼
FAISS Vector Database
      │
      ▼
Semantic Search
      │
      ▼
Candidate Ranking
```

---

# Tech Stack

## Backend

- Python 3.12
- FastAPI
- Uvicorn

## AI & NLP

- Sentence Transformers
- all-MiniLM-L6-v2
- FAISS
- NumPy

## Resume Parsing

- PyPDF
- python-docx

## Database *(Upcoming)*

- PostgreSQL
- SQLAlchemy

## Deployment *(Upcoming)*

- Docker
- Docker Compose
- AWS

---

# Project Structure

```
backend/
│
├── app/
│   ├── api/
│   ├── core/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   │
│   ├── main.py
│   │
│   └── ...
│
├── uploads/
├── test_upload.py
├── test_parser.py
├── test_cleaner.py
├── test_chunk.py
├── test_embedding.py
├── test_vector.py
├── test_ranking.py
│
├── requirements.txt
└── venv/
```

---

# Features Implemented

## Resume Upload

- Upload one or multiple resumes
- PDF support
- DOCX support

---

## Resume Parsing

- Extract text from PDF
- Extract text from DOCX

---

## Text Cleaning

- Remove unwanted spaces
- Remove tabs
- Remove non-printable characters
- Normalize text

---

## Chunking

- Configurable chunk size
- Configurable overlap
- AI-ready chunk generation

---

## Embeddings

Model Used

```
sentence-transformers/all-MiniLM-L6-v2
```

Each chunk is converted into a **384-dimensional embedding vector**.

---

## Vector Search

Using **FAISS** for semantic similarity search.

Stored Information

- Candidate Name
- Resume Name
- Chunk Number
- Chunk Text
- Embedding Vector

---

## Candidate Ranking

Current Version

- Semantic Search
- Top Matching Resume Chunks

Upcoming

- Overall Candidate Score
- Match Percentage
- Skill Matching
- Experience Matching

---

# APIs

## Health Check

```
GET /health
```

---

## Job Description

```
POST /jobs
```

---

## Resume Upload

```
POST /resumes/upload
```

---

# Upcoming Roadmap

- Candidate Score Aggregation
- PostgreSQL Integration
- SQLAlchemy ORM
- Persistent FAISS Index
- Resume Processing Pipeline
- Job Processing Pipeline
- Complete Ranking API
- JWT Authentication
- React Frontend
- Recruiter Dashboard
- Docker
- Docker Compose
- CI/CD
- AWS Deployment
- Monitoring & Logging
- Unit Testing
- Integration Testing
- Production Optimization

---

# Installation

Clone the repository

```bash
git clone https://github.com/pikachu-matrix/ai-resume-screening.git
```

Move into backend

```bash
cd ai-resume-screening/backend
```

Create virtual environment

```bash
python -m venv venv
```

Activate virtual environment

### Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the server

```bash
uvicorn app.main:application --reload
```

Open

```
http://127.0.0.1:8000/docs
```

---

# Current Status

**Development Stage:** AI Backend Foundation Completed

The project currently supports semantic resume search using embeddings and FAISS. The next milestone is implementing candidate score aggregation and complete AI-based candidate ranking.

---

# Author

**Ranjan**

Building an end-to-end production-ready AI Resume Screening System from scratch using modern AI, backend, and deployment technologies.
