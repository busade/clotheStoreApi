from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "ThreadCraft API"
    database_url: str = "sqlite:///./threadcraft.db"
    secret_key: str = "change-this-development-secret"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    cors_origins: list[str] = ["*"]
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
