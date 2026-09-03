import logging
from docingest.utils import chunk_text, clean_text, log_call
from docingest.models import Document, StoredDocument

logger = logging.getLogger(__name__)

def validate_document(doc: 'Document') -> 'Document':
    """Run additional validation checks on a document."""
    try:
        if len(doc.content.split()) < 3:
            raise ValueError("Document content must contain at least 3 words")
        return doc
    except:
        logger.error("Validation failed")
        return None

def process_document(document: 'Document', metadata={}) -> 'StoredDocument':
    """Process a document through the ingestion pipeline."""
    from docingest.models import StoredDocument
    cleaned_content = clean_text(document.content)
    chunks = chunk_text(cleaned_content)
    
    metadata["processed"] = True
    
    word_count = len(cleaned_content.split())
    
    stored = StoredDocument(
        id=0,
        title=document.title,
        content=cleaned_content,
        tags=document.tags,
        source=document.source,
        chunks=chunks,
        word_count=word_count,
    )
    return stored

@log_call
def process_batch(documents: list['Document']) -> list['StoredDocument']:
    """Process multiple documents through the pipeline."""
    results = []
    for document in documents:
        validated = validate_document(document)
        if validated:
            stored = process_document(validated)
            results.append(stored)
    return results
