from langgraph.graph import StateGraph, END
from .analysis_state import AnalysisState
from .nodes import cargar_archivos, analizar_archivo, generar_resumen, quedan_archivos

def build_graph():
    graph = StateGraph(AnalysisState)

   
    graph.add_node("cargar_archivos", cargar_archivos)
    graph.add_node("analizar_archivo", analizar_archivo)
    graph.add_node("generar_resumen", generar_resumen)

    
    graph.set_entry_point("cargar_archivos")
    graph.add_edge("cargar_archivos", "analizar_archivo")

  
    graph.add_conditional_edges(
        "analizar_archivo",
        quedan_archivos,
        {
            "analizar_archivo": "analizar_archivo",
            "generar_resumen": "generar_resumen"
        }
    )

    graph.add_edge("generar_resumen", END)

    return graph.compile()