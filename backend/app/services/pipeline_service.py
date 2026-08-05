from app.services.chunk_service import ChunkService
from app.services.embedding_service import EmbeddingService
from app.services.text_cleaner import TextCleaner
from app.services.parser import ParserService

class PipelineService:

    @staticmethod
    def process_resume(file_path: str,):
        # Extract text from PDF
        text = ParserService.extract_text(file_path)

        # Clean the extracted text
        clean_text = TextCleaner.clean(text)

        # Create chunks from the cleaned text
        chunks = ChunkService.create_chunks(clean_text)

        # Build vector database for the resume
        #vector_db = VectorService()

        embeddings = []

        for chunk in chunks: 
            embedding = EmbeddingService.create_embedding(chunk)
            embeddings.append(
                {
                    "embedding": embedding,
                    "chunk": chunk,
                }
            )

        return embeddings