import faiss
import numpy as np

class VectorService:
    def __init__(self):
        self.dimension=384
        self.index = faiss.IndexFlatL2(self.dimension)  # L2 distance index
        self.metadata =[]

    def add_vector(
            self,
            embedding,
            metadata,
    ):
        embedding=np.array(
            [embedding],
            dtype="float32",
        )
        self.index.add(embedding)
        self.metadata.append(metadata)

    def search(
            self,
            embedding: np.ndarray,
            top_k: int = 3,
    ):
        embedding = np.array(
            [embedding],
            dtype="float32",
        )
        distances, indices = self.index.search(
            embedding,
            top_k,
        )
        results = []
        for distance, index in zip(distances[0], indices[0]):
            if index != -1:
                metadata=self.metadata[index].copy()
                metadata["distance"]=float(distance)
                metadata["similarity"]=round((1/(1+distance))*100,
                2,)
                results.append(
                    metadata)
                
        return results