from functools import lru_cache
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore"
    )

    
    APP_NAME: str="AI Business OS"
    APP_VERSION: str="0.1.0"

    DEBUG: bool=True

    ENVIRONMENT: str="development"

    HOST: str="127.0.0.1"
    

@lru_cache
def get_setting():

    return Settings()
setting = get_setting()



