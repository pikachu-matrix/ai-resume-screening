from app.services.embedding_service import EmbeddingService
class RankingService:
    @staticmethod
    def rank_candidates(
        job_description: str,
        vector_db,
        top_k: int = 5,
    ):
        query_embedding = EmbeddingService.create_embedding(job_description)

        results = vector_db.search(
            query_embedding,
            top_k,)
        return results
    
    