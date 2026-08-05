from pathlib import Path

from app.services.chunk_service import ChunkService
from app.services.embedding_service import EmbeddingService
from app.services.parser import ParserService
from app.services.ranking_service import RankingService
from app.services.text_cleaner import TextCleaner
from app.services.vector_service import VectorService
from app.services.score_service import ScoreService

# Load resume
pdf_file = Path(__file__).parent / "sample.pdf"

text = ParserService.extract_text(str(pdf_file))
clean_text = TextCleaner.clean(text)
chunks = ChunkService.create_chunks(clean_text)

# Build vector database
vector_db = VectorService()

for index, chunk in enumerate(chunks):

    embedding = EmbeddingService.create_embedding(chunk)

    vector_db.add_vector(
        embedding,
        {
            "candidate_name": "Amiya Ranjan Kabi",
            "resume": "sample.pdf",
            "chunk_number": index + 1,
            "text": chunk,
        },
    )

# Job Description
job_description = """
Looking for an AI Engineer with experience in
Python,
FastAPI,
Machine Learning,
SQL,
Docker,
REST APIs.
"""

chunk_results = RankingService.rank_candidates(
    job_description,
    vector_db,
)
results = ScoreService.aggregate(chunk_results)

print("=" * 70)
print("Final Candidate Ranking")
print("=" * 70)

for rank, candidate in enumerate(results, start=1):

    print(f"Rank : {rank}")
    print(
        f"Candidate : {candidate['candidate_name']}"
    )
    print(
        f"Resume : {candidate['resume']}"
    )
    print(
        f"Overall Match : {candidate['overall_match']}%"
    )
    print(
        f"Best Chunk : {candidate['best_chunk']}%"
    )
    print(
        f"Matched Chunks : {candidate['matched_chunks']}"
    )

    print("=" * 70)