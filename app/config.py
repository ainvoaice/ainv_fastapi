# app/config.py
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List
from functools import lru_cache


class _Settings(BaseSettings):
    AIN_SUPA_ASYNC: str = "postgresql+asyncpg://username:pwd@local/icedb"
    OPENAI_API_KEY: str =""
    COHERE_API_KEY: str = ""
    TAVILY_API_KEY: str = ""

    ALLOWED_ORIGINS: List[str] = ["http://localhost:3000", "http://127.0.0.1:3000"]

    STRIPE_SECRET_KEY: str = ""
    STRIPE_WEBHOOK_SECRET: str = ""
    STRIPE_SUCCESS_URL: str = "https://t4agents.com/billing/success"
    STRIPE_CANCEL_URL: str = "https://t4agents.com/billing/cancel"
    STRIPE_PORTAL_RETURN_URL: str = "https://t4agents.com/billing"

    STRIPE_PRICE_BASIC_MONTH: str= "price_1TBOWrRwLzeE6kyCNFmHZzTp"
    STRIPE_PRICE_BASIC_YEAR: str = "price_1TBOWrRwLzeE6kyCprGxdvWK"
    STRIPE_PRICE_PRO_MONTH: str = "price_1TBOaiRwLzeE6kyCV57uGsvn"
    STRIPE_PRICE_PRO_YEAR: str = "price_1TBOaiRwLzeE6kyCgHUak49W"
    STRIPE_PRICE_ENTERPRISE_MONTH: str = "price_1TBOb9RwLzeE6kyCcAgDncr1"
    STRIPE_PRICE_ENTERPRISE_YEAR: str = "price_1TBObXRwLzeE6kyCSWexfBjm"
    
    model_config = SettingsConfigDict(env_file=".env")
    
@lru_cache()
def get_settings_singleton()-> _Settings:
    return _Settings()
