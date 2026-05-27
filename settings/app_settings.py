from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict
from .apis import APIs


class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        extra='ignore',
        env_file_encoding="utf-8",
        env_nested_delimiter="__",
        env_nested_max_split=2,
        case_sensitive=False
    )

    title: str
    apis: APIs


@lru_cache
def get_app_settings() -> AppSettings:
    return AppSettings()  # type: ignore
