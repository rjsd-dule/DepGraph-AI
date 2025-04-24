
import os
import json

def guardar_resultados(nombre_archivo, resultados, carpeta_resultados="resultados"):
    os.makedirs(carpeta_resultados, exist_ok=True)
    ruta = os.path.join(carpeta_resultados, f"{nombre_archivo}.json")
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(resultados, f, indent=4, ensure_ascii=False)