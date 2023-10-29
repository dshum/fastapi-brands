from pathlib import Path

from pydantic_settings import BaseSettings

__all__ = [
    "BASE_DIR",
    "app",
    "db",
    "sentry",
    "ssh",
]

BASE_DIR = Path(__file__).resolve().parent.parent


class AppSettings(BaseSettings):
    class Config:
        case_sensitive = True

    APP_NAME: str = "Brands"
    SECRET_KEY: str = "fake_secret_key"
    BUILD_NUMBER: str = "0"
    DEBUG: bool = False
    ENVIRONMENT: str = "local"
    LOG_LEVEL: str = "INFO"


class DatabaseSettings(BaseSettings):
    class Config:
        env_prefix = "DATABASE_"
        case_sensitive = True

    LOCAL_URL: str
    REMOTE_URL: str
    ECHO: bool = False


class SentrySettings(BaseSettings):
    class Config:
        env_prefix = "SENTRY_"
        case_sensitive = True

    DSN: str = ""
    ENABLE: bool = False
    TRACES_SAMPLE_RATE: float = 0.0


class SshSettings(BaseSettings):
    class Config:
        env_prefix = "SSH_"
        case_sensitive = True

    URL: str
    PRIVATE_SERVER: str
    USER: str
    KEY: str
    SECRET: str


app = AppSettings.model_validate({})
db = DatabaseSettings.model_validate({})
sentry = SentrySettings.model_validate({})
ssh = SshSettings.model_validate({})
