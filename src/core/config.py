from pydantic import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY: str

    class Config:
        case_sensitive: True


settings = Settings()
