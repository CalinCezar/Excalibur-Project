from typing import List
import weaviate
from weaviate.classes.config import Configure, Property, DataType

class WeaviateDB:
    """Handle Weaviate database operations."""
    
    def __init__(self) -> None:
        self.client = weaviate.connect_to_local()
        self.setup_collections()

    def setup_collections(self) -> None:
        """Setup required Weaviate collections."""
        if not self.client.collections.exists("Document"):
            self.client.collections.create(
                name="Document",
                properties=[
                    Property(name="title", data_type=DataType.TEXT),
                    Property(name="body", data_type=DataType.TEXT),
                ],
            )

    def insert_document(self, title: str, body: str, vector: List[float]) -> None:
        """Insert a document with its embedding vector."""
        collection = self.client.collections.get("Document")
        collection.data.insert(
            {"title": title, "body": body},
            vector=vector
        )

    def query_similar(self, query_text: str, limit: int = 5) -> List[str]:
        """Query for similar documents."""
        collection = self.client.collections.get("Document")
        results = collection.query.near_text(
            query=query_text,
            limit=limit,
        )
        return [getattr(doc, "properties").get("body", "") for doc in results.objects]