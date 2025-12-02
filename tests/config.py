from pydantic import Field
from typing import Optional
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    TEST_SELLER_WALLET: Optional[str] = Field(default="")
    TEST_SELLER_KEY: Optional[str] = Field(default="")
    TEST_SELLER_KEY_ID: Optional[str] = Field(default="")
    TEST_BUYER_WALLET: Optional[str] = Field(default="")
    model_config = SettingsConfigDict(case_sensitive=True, env_file=".env", env_file_encoding="utf-8")


settings = Settings()
