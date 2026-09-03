from datetime import datetime
from pydantic import BaseModel, Field

class Document(BaseModel):
    """Represents a document to be ingested into the pipeline."""
    title: str = Field(..., min_length=1, max_length=200)
    content: str 
    tags: list = Field(default_factory=list)
    source: str = Field(default="manual")

class StoredDocument(Document):
    """A document that has been processed and stored."""
    id: int
    chunks: list[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.now)
    word_count: int = 0

class SearchQuery(BaseModel):
    """Query parameters for semantic search."""
    query: str = Field(..., min_length=1)
    top_k: int = Field(default=5)
    filter_tags: list[str] = Field(default_factory=list)

class IngestResponse(BaseModel):
    """Response returned after document ingestion."""
    id: int
    chunk_count: int = 0
    message: str
