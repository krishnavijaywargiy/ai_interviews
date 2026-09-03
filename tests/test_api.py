import pytest
from fastapi.testclient import TestClient

from docingest.main import app


@pytest.fixture
def client():
    return TestClient(app)


@pytest.mark.task_fastapi
class TestFastAPIEndpoints:

    def test_health_check(self, client):
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json() == {"status": "healthy"}

    def test_create_document_returns_201(self, client):
        payload = {
            "title": "Test Doc",
            "content": "This is a test document with enough words.",
            "tags": ["test"],
        }
        response = client.post("/documents", json=payload)
        assert response.status_code == 201

    def test_create_returns_ingest_response(self, client):
        payload = {
            "title": "Test Doc",
            "content": "This is a test document with enough content words.",
            "tags": ["test"],
        }
        response = client.post("/documents", json=payload)
        data = response.json()
        assert "id" in data
        assert "message" in data
        assert "chunk_count" in data

    def test_read_document(self, client):
        payload = {
            "title": "Readable Doc",
            "content": "Content for reading back from the store.",
            "tags": ["read"],
        }
        create_response = client.post("/documents", json=payload)
        document_id = create_response.json()["id"]

        read_response = client.get(f"/documents/{document_id}")
        assert read_response.status_code == 200
        assert read_response.json()["title"] == "Readable Doc"

    def test_read_missing_document_returns_404(self, client):
        response = client.get("/documents/999")
        assert response.status_code == 404
