from app.database import Base, engine
from app.models.job import Job
from app.models.resume import Resume


print("Creating tables...")
Base.metadata.create_all(bind=engine)
print("Tables created successfully.")

