from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class CorsSettings(BaseModel):
    allow_origins: list[str] = [
        "http://localhost",
        "http://localhost:8000",
    ]
    allow_credentials: bool = True
    allow_methods: list[str] = ["*"]
    allow_headers: list[str] = ["*"]


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="APP_",
        env_nested_delimiter="__",
    )

    host: str = "localhost"
    port: int = 8000
    reload: bool = True

    cors: CorsSettings = CorsSettings()


settings = Settings()
