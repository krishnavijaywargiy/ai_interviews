import pytest

from docingest.services import reset_store


@pytest.fixture(autouse=True)
def clean_store():
	"""Reset the document store before and after each test."""
	reset_store()
	yield
	reset_store()
