from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # TODO: Fill in the fields based on the .env file
    # Example:
    # GROQ_API_KEY: str
    # LLM_MODEL: str = "llama-3.1-70b-versatile"
    # LLM_TEMPERATURE: float = 0.7
    pass

settings = Settings()
