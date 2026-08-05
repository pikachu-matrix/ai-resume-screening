from pathlib import Path
from app.services.pipeline_service import PipelineService

#Path to the resume file
pdf_file = Path(__file__).parent / "sample.pdf"

# Process the resume using the PipelineService
processed_resume = PipelineService.process_resume(str(pdf_file))

print("=" * 70)
print("Pipeline Test")
print("=" * 70)
print(f"Total Chunks Processed: {len(processed_resume)}")
print()
print("First Chunk")
print("-" * 70)
print(processed_resume[0]["chunk"][:300])  # Print the first 300 characters of the first chunk
print()
print("Embedding Dimension")
print("-" * 70)
print(len(processed_resume[0]["embedding"]))  # Print the dimension of the embedding for the first chunk