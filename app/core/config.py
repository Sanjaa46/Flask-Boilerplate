from functools import lru_cache

from typing import Literal
from pydantic import SecretStr, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore", case_sensitive=False)

    app_name: str = "Flask Boilerplate"
    environment: Literal["local", "test", "production", "staging"] = "local"
    debug: bool = False
    api_v1_prefix: str = "/api/v1"
    secret_key: SecretStr

    @model_validator(mode="after")
    def _reject_unsafe_production(self) -> "Settings":
        if self.environment == "production":
            if self.debug:
                raise ValueError("DEBUG must be false in production")
            if self.secret_key.get_secret_value() in {"", " ", "change_me", "abc"}:
                raise ValueError("SECRET_KEY must be set to a strong secret in production")
        return self

@lru_cache
def get_settings() -> Settings:
    return Settings()