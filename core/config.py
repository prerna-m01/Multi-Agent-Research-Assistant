from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    GOOGLE_API_KEY: str

    TAVILY_API_KEY: str

    DATABASE_URL: str = "sqlite:///research.db"

    class Config:
        env_file = ".env"


settings = Settings()