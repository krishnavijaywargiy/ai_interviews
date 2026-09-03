import pytest
from pydantic import ValidationError


@pytest.mark.task_pydantic
class TestDocumentModel:

    def test_valid_document(self):
        from docingest.models import Document

        document = Document(
            title="Test Document",
            content="Valid content for the document.",
            tags=["ai", "testing"],
        )
        assert document.title == "Test Document"
        assert document.source == "manual"
        assert isinstance(document.tags, list)

    def test_tags_reject_non_strings(self):
        from docingest.models import Document

        with pytest.raises(ValidationError):
            Document(title="Test", content="Valid content here for testing.", tags=[1, 2, 3])

    def test_empty_content_rejected(self):
        from docingest.models import Document

        with pytest.raises(ValidationError):
            Document(title="Test", content="", tags=["test"])


@pytest.mark.task_pydantic
class TestSearchQueryModel:

    def test_valid_query(self):
        from docingest.models import SearchQuery

        query = SearchQuery(query="machine learning", top_k=10)
        assert query.top_k == 10

    def test_top_k_minimum(self):
        from docingest.models import SearchQuery

        with pytest.raises(ValidationError):
            SearchQuery(query="test", top_k=0)

    def test_top_k_maximum(self):
        from docingest.models import SearchQuery

        with pytest.raises(ValidationError):
            SearchQuery(query="test", top_k=101)
