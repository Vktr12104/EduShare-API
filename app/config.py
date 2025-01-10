from functools import lru_cache
from pydantic_settings import BaseSettings


DB = "mysql+pymysql://root:Viktor12@localhost:3306/tangguhpos_auth"
class Config(BaseSettings):
    ACCESS_TOKEN_EXPIRATION: int = 5 * 60
    REFRESH_TOKEN_EXPIRATION: int = 1 * 24 * 60 * 60
    PRIVATE_KEY: str
    PUBLIC_KEY: str
    REFRESH_PRIVATE_KEY: str


    class Config:
        env_file = '.env'

@lru_cache
def get_config():
    return Config()

config = get_config()
