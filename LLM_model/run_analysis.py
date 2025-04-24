#from .core.graph_builder import build_graph
#from .core.analysis_state import initial_state
#from .config.settings import settings

from LLM_model.core.graph_builder import build_graph
from LLM_model.core.analysis_state import initial_state
from LLM_model.config.settings import settings

def run_analysis():
    print(" Iniciando análisis de código...")
    
    # Construir y compilar el grafo
    analizador_app = build_graph()
    
    # Ejecutar el grafo
    result = analizador_app.invoke(initial_state())
    
    # Guardar y mostrar resultados
    with open(settings.OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(result["resultado_final"])
    
    print("\n Análisis completado!")
    print(f" Resultado guardado en: {settings.OUTPUT_FILE}")
    print("\n--- Vista previa ---")
    print(result["resultado_final"][:1000] + "...")

if __name__ == "__main__":
    run_analysis()