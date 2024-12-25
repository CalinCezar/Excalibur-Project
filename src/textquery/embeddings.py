from typing import List
from sentence_transformers import SentenceTransformer

class EmbeddingGenerator:
    """Handle text embedding generation."""
    
    def __init__(self, model_name: str = "all-MiniLM-L6-v2") -> None:
        self.model = SentenceTransformer(model_name)
    
    def generate(self, text: str) -> List[float]:
        """Generate embeddings for given text."""
        return self.model.encode(text).tolist()
    
    def generate_batch(self, texts: List[str]) -> List[List[float]]:
        """Generate embeddings for a batch of texts."""
        return self.model.encode(texts).tolist()