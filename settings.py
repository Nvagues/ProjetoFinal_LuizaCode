from pydantic import BaseSettings
from decouple import config

class Config(BaseSettings):
    DATABASE_URI = config("DATABASE_URI")
    
settings= Config()