# AI Engineer Coding Interview

## Scenario

DocIngest is a document ingestion and search API for an AI/RAG pipeline. It accepts documents, validates them with Pydantic, processes them through a text pipeline (cleaning, chunking), stores them in memory, and exposes FastAPI endpoints for retrieval and search.

The codebase has several bugs across different layers. Your job is to find and fix them.

## Rules

*   **No automated coding assistants**
*   Google, Stack Overflow, and official documentation are allowed
*   Reference links are provided in `docs/references.md`
*   **Time limit: 25 minutes**
*   Work through the tasks in order — later tasks depend on earlier fixes

All candidates work through the same six tasks regardless of level. Scoring considers both completion and the quality/reasoning behind each fix.

## Getting Started

1.  **Create and activate a virtual environment**
    `python -m venv .venv`
    `source .venv/bin/activate`  # Windows: `.venv\Scripts\activate`
2.  **Install the project and its dev dependencies**
    `pip install -e ".[dev]"`

3.  **Run the test suite to see current failures**
    `pytest -v`

4.  **Work through the tasks below, then check your score**
    `python score.py`

> You may encounter an error during installation. Fixing it is Task 1!

## Project Structure

```text
src/docingest/  Application package and processing pipeline
tests/          Marked challenge tests and Task 6 stubs
docs/           Permitted reference documentation
```

## Tasks

| Task | Area | Points | File |
| :--- | :--- | :--- | :--- |
| 1 | Environment Setup | 10 | `pyproject.toml` |
| 2 | Pydantic Models | 15 | `src/docingest/models.py` |
| 3 | FastAPI Endpoints | 15 | `src/docingest/main.py` |
| 4 | Python Fundamentals | 10 | `src/docingest/utils.py` |
| 5 | Exception Handling | 15 | `src/docingest/pipeline.py` |
| 6 | Write Tests | 15 | `tests/test_pipeline.py` |

**Task 1 — Environment Setup (10 pts)** Create and activate a virtual environment, then fix the dependency issue so `pip install -e ".[dev]"` succeeds.

**Task 2 — Pydantic Models (15 pts)** Fix the model validation bugs in `src/docingest/models.py`.
*   `Document.tags` should only accept lists of strings
*   Empty document content should be rejected
*   `SearchQuery.top_k` should be bounded between 1 and 100

**Task 3 — FastAPI Endpoints (15 pts)** Fix the API bugs in `src/docingest/main.py`.
*   `POST /documents` should return HTTP 201 on success
*   `GET /documents/{doc_id}` should accept integer IDs
*   `GET /documents/{doc_id}` should return HTTP 404 for missing documents

**Task 4 — Python Fundamentals (10 pts)** Fix the utility bugs in `src/docingest/utils.py`.
*   The `@log_call` decorator should preserve the wrapped function's metadata
*   The `batch_items` generator should yield all items including the last incomplete batch

**Task 5 — Exception Handling (15 pts)** Fix the exception handling bugs in `src/docingest/pipeline.py`.
*   `validate_document` should propagate validation errors, not swallow them
*   `process_document` should not use a mutable default argument

**Task 6 — Write Tests (15 pts)** Implement the two test stubs in the `TestWriteTests` class in `tests/test_pipeline.py`. Each stub has a docstring describing what to test.

Fix Tasks 1-5 before attempting Task 6.

## Check Your Score

```bash
python score.py