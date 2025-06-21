from typing import List

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Project Information
    PROJECT_NAME: str = "FastAPI Learning Project"
    VERSION: str = "1.0.0"
    DESCRIPTION: str = "A FastAPI project with best practices structure"

    # API Configuration
    API_V1_STR: str = "/api/v1"

    # CORS Settings
    BACKEND_CORS_ORIGINS: str = ""

    def get_cors_origins(self) -> List[str]:
        """Parse CORS origins from string to list"""
        if (
            not self.BACKEND_CORS_ORIGINS
            or self.BACKEND_CORS_ORIGINS.strip() == ""
        ):
            return []
        return [
            origin.strip()
            for origin in self.BACKEND_CORS_ORIGINS.split(",")
            if origin.strip()
        ]

    # Database Configuration
    DATABASE_URL: str = "sqlite:///./app.db"

    # Security Settings
    SECRET_KEY: str = "your-secret-key-here-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Superuser Configuration
    FIRST_SUPERUSER: str = "admin@example.com"
    FIRST_SUPERUSER_PASSWORD: str = "changethis"

    # Development Settings
    DEBUG: bool = True
    LOG_LEVEL: str = "INFO"

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
