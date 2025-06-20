import os
from dotenv import load_dotenv

load_dotenv()  # Carga .env al entorno

class Settings:
    APP_NAME: str = "Sistema Experto Médico"
    VERSION: str = "1.0.0"
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    USE_DATABASE: bool = os.getenv("USE_DATABASE", "false").lower() == "true"

settings = Settings()
