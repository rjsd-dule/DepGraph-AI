import json
import os
import patrones
import alldef
import outputConsole
#import guardar_resultados
from guardar_resultados import guardar_resultados
import graph


def analizar_proyecto(directorio_base):
    dependencias = {}
    archivos_proyecto = set()
    todos_los_imports = set()
    archivo_code=set()

    # Paso 1: Recolectar todos los archivos del proyecto
    for root, _, archivos in os.walk(directorio_base):
        for archivo in archivos:
            nombre_sin_ext = alldef.obtener_nombre_sin_ruta_ni_extension(os.path.splitext(archivo)[0])
            file_name = alldef.obtener_nombre_sin_ruta_ni_extension(archivo)
            archivos_proyecto.add(nombre_sin_ext) 
            archivo_code.add(file_name)

    # Paso 2: Procesar cada archivo
    for root, _, archivos in os.walk(directorio_base):
        for archivo in archivos:
            ruta_completa = os.path.join(root, archivo)
            nombre_archivo, extension = alldef.extraer_extension_y_nombre(ruta_completa)
            nombre_sin_ext = alldef.obtener_nombre_sin_ruta_ni_extension(os.path.splitext(archivo)[0])

            if extension in patrones.PATRONES_POR_EXTENSION:
                #print(f"\nAnalizando: {ruta_completa}")
                try:
                    texto = alldef.cargar_codigo(ruta_completa)
                    resultados = alldef.procesar_patrones(extension, texto)
                    
                    if nombre_sin_ext not in dependencias:
                        dependencias[nombre_sin_ext] = []
                    
                    # Dentro de analizar_proyecto(), modifica el bloque de procesamiento:
                    for modulo in resultados.get("importaciones", []):
                        # Normaliza el nombre del módulo (sin .py ni rutas)
                        modulo_limpio = os.path.splitext(modulo)[0]
                        
                        # Registrar todos los imports
                        todos_los_imports.add(modulo_limpio)
                        
                        # Verificar si es un archivo local
                        if modulo_limpio in archivos_proyecto and modulo_limpio != nombre_sin_ext:
                            if modulo_limpio not in dependencias[nombre_sin_ext]:
                                dependencias[nombre_sin_ext].append(modulo_limpio)
                                #print(f"DEPENDENCIA: {nombre_sin_ext} -> {modulo_limpio}")

                    guardar_resultados(nombre_archivo, resultados)
                except Exception as e:
                    print(f"[ERROR] En {archivo}: {str(e)}")

    # Paso 3: Clasificar dependencias
    dependencias_externas = {
        archivo: [imp for imp in imports if imp not in archivos_proyecto]
        for archivo, imports in dependencias.items()
    }

    dependencias_internas = {
        archivo: [imp for imp in imports if imp in archivos_proyecto]
        for archivo, imports in dependencias.items()
    }

    # Paso 4: Generar resultados
    resultados = {
        "dependencias_internas": dependencias_internas,
        "dependencias_externas": dependencias_externas,
        "todos_los_imports": sorted(list(todos_los_imports)),
        "archivos_del_proyecto": sorted(list(archivo_code))
    }

    os.makedirs("resultados_dependencias", exist_ok=True)
    with open("resultados_dependencias/dependencias.json", "w", encoding="utf-8") as f:
        json.dump(resultados, f, indent=4, ensure_ascii=False)

    # Generar gráfico con NetworkX solo para dependencias internas
    if any(dependencias_internas.values()):
        graph.generar_grafico_con_networkx(
            {k: v for k, v in dependencias_internas.items() if v},
            "dependencias_internas"
        )


    print("\n=== Resumen del análisis ===")
    print(f"Archivos analizados: {len(archivos_proyecto)}")
    print(f"Dependencias internas encontradas: {sum(len(v) for v in dependencias_internas.values())}")
    print(f"Dependencias externas encontradas: {sum(len(v) for v in dependencias_externas.values())}")
    outputConsole.mostrar_resultados_mejorados(resultados)


def main():
    analizar_proyecto("code")

if __name__ == "__main__":
    main()