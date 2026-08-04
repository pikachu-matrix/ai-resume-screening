from app.services.chunk_service import ChunkService
from app.services.parser import ParserService
from app.services.text_cleaner import TextCleaner

text = ParserService.extract_text("sample.pdf")

clean_text = TextCleaner.clean(text)

chunks = ChunkService.create_chunks(clean_text)

print(f"Total Chunks : {len(chunks)}")

for index, chunk in enumerate(chunks):

    print("=" * 60)

    print(f"Chunk {index + 1}")

    print(chunk)