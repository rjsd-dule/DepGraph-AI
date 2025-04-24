import json
import sys
from jinja2 import Template
from langchain_google_genai import ChatGoogleGenerativeAI
from LLM_model.config.settings import settings
import os
class LLMService:
    def __init__(self):
        ruta_base = os.path.dirname(__file__)
        ruta_archivo = os.path.join(ruta_base, "build_prompt.jinja2")
        with open(ruta_archivo, "r", encoding="utf-8") as f:
            self.jinja_template = Template(f.read())
        
        self.llm = ChatGoogleGenerativeAI(
            model=settings.GEMINI_MODEL,
            temperature=settings.TEMPERATURE,
            api_key=settings.GEMINI_API_KEY
        )
    
    def generate_analysis(self, nombre_funcion: str, archivo_name: str, dependencias: list, codigo_fuente: str) -> str:
        try:
            rendered_prompt = self.jinja_template.render(
                archivo_name=archivo_name,
                nombre_funcion=nombre_funcion,
                dependencias=dependencias,
                codigo_fuente=codigo_fuente
            )
            prompt_data = json.loads(rendered_prompt)
            response = self.llm.invoke(json.dumps(prompt_data, ensure_ascii=False, indent=2))
            return response.content
        except json.JSONDecodeError as e:
            raise ValueError(f"Error en JSON: {str(e)}")
        except Exception as e:
            raise RuntimeError(f"Error generando análisis: {str(e)}")