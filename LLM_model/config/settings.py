import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

class Settings:
    
    GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-1.5-pro-latest")
    TEMPERATURE = float(os.getenv("TEMPERATURE", 0.7))
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    
    BASE_DIR = Path(__file__).parent.parent.parent 
    CODE_FOLDER = BASE_DIR / "analysercode"
    DEPENDENCIES_PATH = BASE_DIR / "resultados"
    OUTPUT_FILE = BASE_DIR / "final_analysis.md"
    

settings = Settings()