import sys

import pytest


@pytest.mark.task_setup
class TestEnvironmentSetup:

    def test_running_in_virtual_environment(self):
        """Tests should run inside a virtual environment."""
        assert sys.prefix != sys.base_prefix, (
            "Create and activate a virtual environment: python -m venv .venv"
        )

    def test_docingest_imports(self):
        """All docingest modules should be importable."""
        try:
            import docingest.main
            import docingest.models
            import docingest.pipeline
            import docingest.services
            import docingest.utils
        except ImportError as error:
            pytest.fail(f"Failed to import docingest module: {error}")

    def test_fastapi_app_exists(self):
        from docingest.main import app

        assert app.title == "DocIngest API"