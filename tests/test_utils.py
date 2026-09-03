import pytest


@pytest.mark.task_python
class TestLogCallDecorator:

    def test_preserves_function_name(self):
        from docingest.utils import log_call

        @log_call
        def my_function():
            return 42

        assert my_function.__name__ == "my_function"

    def test_preserves_docstring(self):
        from docingest.utils import log_call

        @log_call
        def my_function():
            """My docstring."""
            return 42

        assert my_function.__doc__ == "My docstring."

    def test_returns_correct_value(self):
        from docingest.utils import log_call

        @log_call
        def add(first, second):
            return first + second

        assert add(2, 3) == 5


@pytest.mark.task_python
class TestBatchItems:

    def test_includes_last_incomplete_batch(self):
        from docingest.utils import batch_items

        assert list(batch_items([1, 2, 3, 4, 5], 2)) == [[1, 2], [3, 4], [5]]
