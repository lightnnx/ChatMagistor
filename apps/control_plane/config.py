from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "Telegram Archive"
    APP_VERSION: str = "0.1.0"
    ENVIRONMENT: str = "development"

    HOST: str = "0.0.0.0"
    PORT: int = 8000

    DATABASE_URL: str = (
        "postgresql+asyncpg://archive:archive_dev_password"
        "@localhost:5432/telegram_archive"
    )

    NODE_HEARTBEAT_INTERVAL: int = 15
    NODE_TIMEOUT: int = 60

    ENROLLMENT_TOKEN_TTL: int = 300

    APP_SECRET: str = "CHANGE_THIS_TO_A_RANDOM_SECRET"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )


settings = Settings()
