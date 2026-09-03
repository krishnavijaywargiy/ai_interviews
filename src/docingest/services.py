import logging
from docingest.models import Document, IngestResponse, StoredDocument
from docingest.pipeline import process_document, validate_document

logger = logging.getLogger(__name__)

_document_store: dict[int, StoredDocument] = {}
_next_id = 1

def ingest_document(document: Document) -> IngestResponse:
    """Validate, process, and store a document."""
    global _next_id

    validated = validate_document(document)
    if not validated:
        raise ValueError("Document validation failed")
    
    stored = process_document(validated)
    stored.id = _next_id
    _document_store[_next_id] = stored
    _next_id += 1

    logger.info(f"Stored document {stored.id}: {stored.title}")

    return IngestResponse(
        id=stored.id,
        chunk_count=len(stored.chunks),
        message="Document ingested successfully"
    )

def get_document(doc_id: int) -> StoredDocument | None:
    """Retrieve a document by its ID."""
    return _document_store.get(doc_id)

def search_documents(
    query: str, top_k: int = 5, filter_tags: list[str] | None = None
) -> list[StoredDocument]:
    """Search documents by keyword matching."""
    results = []
    query_lower = query.lower()

    for doc in _document_store.values():
        if filter_tags:
            if not any(tag in doc.tags for tag in filter_tags):
                continue
        
        if query_lower in doc.content.lower() or query_lower in doc.title.lower():
            results.append(doc)
            
    return results[:top_k]

def reset_store():
    """Reset the document store. Used for testing."""
    global _next_id
    _document_store.clear()
    _next_id = 1
