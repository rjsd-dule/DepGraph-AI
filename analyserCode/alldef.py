import patrones
import os
import re
import ast

def cargar_codigo(ruta_archivo):
    """Cargar el contenido de un archivo en formato texto."""
    with open(ruta_archivo, "r", encoding="utf-8") as f:
        return f.read()

def extraer_extension_y_nombre(path):
    """Extraer el nombre y la extensión del archivo dado."""
    nombre_archivo, extension = os.path.splitext(path)
    return os.path.basename(nombre_archivo), extension

def obtener_nombre_sin_ruta_ni_extension(ruta):
    """Obtener solo el nombre del archivo."""
    nombre_archivo = os.path.basename(ruta)
    #return os.path.splitext(nombre_archivo)[0]
    return nombre_archivo

def procesar_patrones(extension, texto):
    patrones_extension = patrones.PATRONES_POR_EXTENSION.get(extension)
    resultado = {
        "importaciones": [],
        "exportaciones": {}
    }

    if not patrones_extension:
        print(f"[!] No hay patrones definidos para la extensión '{extension}'\n")
        return {}

    for tipo, patron in patrones_extension.items():
        if tipo == "importaciones":
            for match in re.finditer(patron, texto, re.MULTILINE):
                modulo = match.group(1) if match.group(1) else match.group(2)
                if modulo:
                    modulo_limpio = modulo.split('.')[-1]
                    resultado["importaciones"].append(modulo_limpio)
                    #print(f"Importación detectada: {modulo_limpio}")

    # Extrae las exportaciones del archivo (funciones, clases, variables públicas)
    resultado["exportaciones"] = obtener_exportaciones(texto)

    return resultado

def obtener_exportaciones(texto_codigo):
    exportaciones = {
        "funciones": [],
        "clases": [],
        "variables": []
    }

    try:
        tree = ast.parse(texto_codigo)
        for nodo in tree.body:
            if isinstance(nodo, ast.FunctionDef):
                if not nodo.name.startswith("_"):
                    exportaciones["funciones"].append(nodo.name)
            elif isinstance(nodo, ast.ClassDef):
                if not nodo.name.startswith("_"):
                    exportaciones["clases"].append(nodo.name)
            elif isinstance(nodo, ast.Assign):
                for target in nodo.targets:
                    if isinstance(target, ast.Name):
                        if not target.id.startswith("_"):
                            exportaciones["variables"].append(target.id)
    except Exception as e:
        print(f"[ERROR al extraer exportaciones]: {e}")

    return exportaciones