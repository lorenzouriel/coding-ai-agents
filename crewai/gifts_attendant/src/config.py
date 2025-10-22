from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    """Centralized configuration for the CrewAI project."""
    
    # Core environment
    ENV: str = Field(default="development", description="Environment name")
    DEBUG: bool = Field(default=True, description="Enable debug mode")
    LOG_LEVEL: str = Field(default="INFO")

    # AI and model configuration
    MODEL_NAME: str = Field(default="gpt-4o-mini", description="Default model for CrewAI")
    OPENAI_API_KEY: str = Field(default="", description="OpenAI API key")

    # Data paths
    CATALOG_INDEX: str = Field(default="data/catalog.csv")
    PRICING_RULES_JSON: str = Field(default="data/pricing_rules.json")

    # Networking / API
    HOST: str = Field(default="0.0.0.0")
    PORT: int = Field(default=8000)

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

# Singleton instance for global import
settings = Settings()
