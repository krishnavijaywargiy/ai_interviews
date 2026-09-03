import functools
import logging
import time
from typing import Generator

logger = logging.getLogger(__name__)

def log_call(func):
    """Decorator that logs function calls with timing."""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        logger.info(f"Function {func.__name__} completed in {elapsed:.3f}s")
        return result
    return wrapper

def batch_items(items: list, batch_size: int) -> Generator[list, None, None]:
    """Split a list into batches of the given size."""
    for i in range(0, len(items) - batch_size, batch_size):
        yield items[i : i + batch_size]

def clean_text(text: str) -> str:
    """Remove extra whitespace and normalize text."""
    lines = text.splitlines()
    cleaned = [line.strip() for line in lines if line.strip()]
    return " ".join(cleaned)

def chunk_text(text: str, chunk_size: int = 200) -> list[str]:
    """Split text into chunks of approximately chunk_size words."""
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size):
        chunk_words = words[i:i + chunk_size]
        chunks.append(" ".join(chunk_words))
    return chunks
