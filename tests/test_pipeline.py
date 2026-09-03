import pytest
import inspect

from docingest.models import Document
from docingest.pipeline import process_document, validate_document

@pytest.mark.task_exceptions
class TestValidateDocument:
    
    def test_valid_document_passes(self):
        doc = Document(
            title="Valid",
            content="This document has enough words to pass validation.",
            tags=["test"]
        )
        result = validate_document(doc)
        assert result is not None
        assert result.title == "Valid"
        
    def test_short_content_raises_error(self):
        doc = Document(
            title="Short",
            content="Two words",
            tags=["test"]
        )
        with pytest.raises(ValueError, match="at least 3 words"):
            validate_document(doc)

    def test_does_not_swallow_exceptions(self):
        doc = Document(title="Short", content="Two words", tags=["test"])
        with pytest.raises(ValueError):
            validate_document(doc)


@pytest.mark.task_exceptions
class TestProcessDocument:
    
    def test_mutable_default_not_used(self):
        from docingest.pipeline import process_document
        
        sig = inspect.signature(process_document)
        default = sig.parameters["metadata"].default
        
        if default is inspect.Parameter.empty:
            return
        assert not isinstance(default, (dict, list, set)), \
            "Use None as default instead of a mutable object"


@pytest.mark.task_testing
class TestWriteTests:
    
    def test_chunk_text_multiple_chunks(self):
        """Verify chunk_text splits long text into multiple chunks."""
        raise NotImplementedError("Implement this test")
        
    def test_chunk_text_short_text_single_chunk(self):
        """Verify chunk_text returns a single chunk for short text."""
        raise NotImplementedError("Implement this test")
