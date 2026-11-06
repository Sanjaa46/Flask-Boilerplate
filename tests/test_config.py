import pytest
from pydantic import ValidationError

from app.core.config import Settings

STRONG_SECRET = "x" * 32


def test_production_reject_debug() -> None:
    with pytest.raises(ValidationError, match="DEBUG"):
        Settings(_env_file=None, environment="production", debug=True, secret_key=STRONG_SECRET)

@pytest.mark.parametrize("secret", ["", " ", "abc", "x"*31])
def test_production_reject_weak_secret(secret: str) -> None:
    with pytest.raises(ValidationError, match="SECRET_KEY"):
        Settings(_env_file=None, environment="production", debug=False, secret_key=secret)

def test_production_accept_configs() -> None:
    settings = Settings(_env_file=None, environment="production", debug=False, secret_key=STRONG_SECRET)
    assert settings.environment == "production"
    assert settings.secret_key.get_secret_value() == STRONG_SECRET

@pytest.mark.parametrize("secret", ["", " ", "abc"])
def test_local_accept_configs(secret: str) -> None:
    settings = Settings(_env_file=None, environment="local", debug=True, secret_key=secret)
    assert settings.environment == "local"
    assert settings.secret_key.get_secret_value() == secret