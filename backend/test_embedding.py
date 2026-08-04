from app.services.chunk_service import ChunkService
from app.services.embedding_service import EmbeddingService
from app.services.parser import ParserService
from app.services.text_cleaner import TextCleaner 


text=ParserService.extract_text("sample.pdf")
clean_text=TextCleaner.clean(text)

chunks=ChunkService.create_chunks(clean_text)

embedding=EmbeddingService.create_embedding(chunks[0])

print(type(embedding))
print(len(embedding))
print(embedding[:10])

