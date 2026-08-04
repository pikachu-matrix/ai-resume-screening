from app.services.chunk_service import ChunkService
from app.services.embedding_service import EmbeddingService
from app.services.parser import ParserService
from app.services.text_cleaner import TextCleaner
from app.services.vector_service import VectorService

from pathlib import Path

pdf_file = Path(__file__).parent / "sample.pdf"

text = ParserService.extract_text(str(pdf_file))

clean_text = TextCleaner.clean(text)

chunks = ChunkService.create_chunks(clean_text)

vector_db = VectorService()

for chunk in chunks:

    embedding = EmbeddingService.create_embedding(chunk)

    vector_db.add_vector(
        embedding,
        chunk,
    )

query = "Python Machine Learning FastAPI"

query_embedding = EmbeddingService.create_embedding(query)

results = vector_db.search(query_embedding)

print("=" * 60)

print("Top Matching Chunks")

print("=" * 60)

for result in results:

    print(result)

    print("-" * 60)