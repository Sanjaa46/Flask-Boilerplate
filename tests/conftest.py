import pytest
from app import create_app
from app.core.config import Settings

@pytest.fixture()
def app():
    """Create Flask app with test configuration"""
    app = create_app(
        Settings(_env_file=None, environment="test", debug=False, secret_key="32_lenght_very_strong_secret_key")  # pyright: ignore[reportCallIssue]  -- runtime option of BaseSettings
    )

    return app


@pytest.fixture()
def client(app):
    return app.test_client()