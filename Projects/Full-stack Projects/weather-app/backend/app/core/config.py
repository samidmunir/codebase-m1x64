from pydantic import BaseSettings

class Settings(BaseSettings):
    weatherstack_api_key: str
    
    class Config:
        env_file = '.env'

settings = Settings()