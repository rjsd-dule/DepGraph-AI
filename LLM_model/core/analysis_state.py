from typing import TypedDict, List, Dict, Optional

class AnalysisState(TypedDict):
    archivos_pendientes: List[Dict]  # Archivos por procesar
    archivos_procesados: List[Dict]  # Resultados por archivo
    resultado_final: Optional[str]   # Resumen consolidado

def initial_state() -> AnalysisState:
    return {
        "archivos_pendientes": [],
        "archivos_procesados": [],
        "resultado_final": None
    }