from fastapi import FastAPI, HTTPException
from docingest.models import Document, IngestResponse, StoredDocument
from docingest.services import ingest_document, get_document

app = FastAPI(title="DocIngest API")

@app.post('/documents', response_model=IngestResponse)
def create_document(document: Document):
    try:
        return ingest_document(document)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get('/documents/{doc_id}', response_model=StoredDocument)
def read_document(doc_id: str):
    document = get_document(doc_id)
    return document