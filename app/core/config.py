from pydantic import Field
from pydantic_settings import SettingsConfigDict, BaseSettings


class Setting(BaseSettings):
    Database_url: str = ""
    JWT_ALGORITHM: str = Field("", alias="algorithm")
    JWT_SECRET_KEY: str = Field("", alias="secret_key")
    JWT_DEFAULT_EXP_MINUTES: int = Field(30, alias="access_token_expire_minutes")
    JWT_REFRESH_EXP_DAYS: int = Field(7, alias="refresh_token_expire_days")
    STRIPE_SECRET_KEY: str = ""
    STRIPE_WEBHOOK_SECRET: str = ""
    REDIS_URL: str = "redis://localhost:6379/0"

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", case_sensitive=False, extra="ignore"
    )


settings = Setting()
