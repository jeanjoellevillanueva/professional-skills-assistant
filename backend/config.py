from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Configurations for the project.
    """

    DATABASE_URL: str
    OPENAI_API_KEY: str

    class Config:
        env_file = '.env'


settings = Settings()
