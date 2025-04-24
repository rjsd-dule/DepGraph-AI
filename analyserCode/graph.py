import networkx as nx
import matplotlib.pyplot as plt
def generar_grafico_con_networkx(dependencias, nombre_archivo="dependencias_networkx"):
    G = nx.DiGraph()  # Grafo dirigido

    # Crear nodos y aristas
    for archivo, imports in dependencias.items():
        G.add_node(archivo)
        for imp in imports:
            G.add_edge(archivo, imp)

    # Dibujar el grafo
    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(G, k=0.5, iterations=50)
    nx.draw(G, pos, with_labels=True, arrows=True, node_color='skyblue',
            edge_color='gray', node_size=2000, font_size=10, font_weight='bold')
    
    plt.title("Grafo de dependencias internas")
    plt.savefig(f"resultados_dependencias/{nombre_archivo}.png", format="png")
    plt.show()