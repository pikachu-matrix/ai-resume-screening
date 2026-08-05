from collections import defaultdict

class ScoreService:
    @staticmethod
    def aggregate(results):
        candidates = defaultdict(list)
        for result in results:

            candidates[
                result["candidate_name"]
            ].append(result)
            final_results = []

        for candidate_name, chunks in  candidates.items():
            similarities=[
                chunk["similarity"] 
                for chunk in chunks
            ]
            average_score = round(sum(similarities)/len(similarities),
                                  2,)

            final_results.append(
                {
                    "candidate_name": candidate_name,
                    "resume": chunks[0]["resume"],
                    "overall_match": average_score,
                    "matched_chunks": len(chunks),
                    "best_chunk" : max(similarities),
                }
            )
        final_results.sort(
            key=lambda x: x["overall_match"],
            reverse=True,
        )

        return final_results