from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

Database_URL = (
    "postgresql+psycopg://postgres:Amiya%402804@localhost:5432/ai_resume_screening"
)

engine = create_engine(Database_URL,)

SessionLocal = sessionmaker(autocommit=False, 
                            autoflush=False, 
                            bind=engine,)

Base = declarative_base()