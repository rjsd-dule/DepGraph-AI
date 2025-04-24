import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-1.5-pro-latest")
    TEMPERATURE = float(os.getenv("TEMPERATURE", 0.7))
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    CODE_FOLDER = ".././analysercode"
    DEPENDENCIES_PATH = ".././resultados"
    OUTPUT_FILE = "analisis_final.md"

settings = Settings()