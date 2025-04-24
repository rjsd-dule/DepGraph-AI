import os
import json
from typing import Dict
from ..config.settings import settings
from .analysis_state import AnalysisState
from .llm_service import LLMService

llm_service = LLMService()

def cargar_archivos(state: AnalysisState) -> Dict:
    """Nodo inicial: Carga todos los archivos a procesar"""
    archivos_data = []
    
    for archivo in os.listdir(settings.CODE_FOLDER):
        ruta_completa = os.path.join(settings.CODE_FOLDER, archivo)
        if os.path.isfile(ruta_completa):
            nombre, _ = os.path.splitext(archivo)
            archivo_datos = os.path.join(settings.DEPENDENCIES_PATH, nombre + ".json")
            
            if os.path.exists(archivo_datos):
                with open(ruta_completa, "r", encoding="utf-8") as codeFile:
                    codigo_fuente = codeFile.read()
                with open(archivo_datos, 'r', encoding='utf-8') as f:
                    datos = json.load(f)
                
                archivos_data.append({
                    "nombre": archivo,
                    "codigo": codigo_fuente,
                    "dependencias": datos.get("importaciones", []),
                    "funciones": datos.get("exportaciones", {}).get("funciones", [])
                })
    
    return {"archivos_pendientes": archivos_data, "archivos_procesados": []}

def analizar_archivo(state: AnalysisState) -> Dict:
    """Nodo: Procesa un archivo (todas sus funciones)"""
    archivo = state["archivos_pendientes"].pop(0)
    resultados_funciones = []
    
    print(f"\n Analizando archivo: {archivo['nombre']}")
    
    for funcion in archivo["funciones"]:
        try:
            analisis = llm_service.generate_analysis(
                nombre_funcion=funcion,
                archivo_name=archivo["nombre"],
                dependencias=archivo["dependencias"],
                codigo_fuente=archivo["codigo"]
            )
            resultados_funciones.append(f"### {funcion}\n{analisis}\n")
        except Exception as e:
            resultados_funciones.append(f"### {funcion}\n Error: {str(e)}\n")
    
    archivo_procesado = {
        "nombre": archivo["nombre"],
        "resultado": "\n".join(resultados_funciones)
    }
    
    return {
        "archivos_procesados": [*state["archivos_procesados"], archivo_procesado],
        "archivos_pendientes": state["archivos_pendientes"]
    }

def generar_resumen(state: AnalysisState) -> Dict:
    """Nodo final: Consolida todos los resultados"""
    resumen = "# Resumen General del Análisis\n\n"
    
    for archivo in state["archivos_procesados"]:
        resumen += f"## {archivo['nombre']}\n{archivo['resultado']}\n"
    
    return {"resultado_final": resumen}

def quedan_archivos(state: AnalysisState) -> str:
    return "analizar_archivo" if state["archivos_pendientes"] else "generar_resumen"