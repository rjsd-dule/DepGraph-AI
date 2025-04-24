def mostrar_resultados_mejorados(resultados):
    """Muestra los resultados del análisis en un formato más legible"""
    print("\n" + "="*50)
    print("ANÁLISIS DE DEPENDENCIAS")
    print("="*50)
    
    # Dependencias internas
    print("\n DEPENDENCIAS ENTRE ARCHIVOS LOCALES:")
    has_deps = False
    count=0
    for archivo, deps in resultados["dependencias_internas"].items():
        if deps:
            has_deps = True
            count+=1
            print(f" {count} {archivo}.py depende de:")
            for dep in deps:
                print(f"  ├─ {dep}.py")
    if not has_deps:
        print("No se encontraron dependencias entre archivos locales")
    
    # Dependencias externas
    print("\n MÓDULOS EXTERNOS IMPORTADOS:")
    externas = sorted(set(resultados["todos_los_imports"]) - set(resultados["archivos_del_proyecto"]))
    print(", ".join(externas) if externas else "Ninguna dependencia externa detectada")
    
    # Archivos aislados
    aislados = [a for a in resultados["archivos_del_proyecto"] 
               if not resultados["dependencias_internas"].get(a, []) 
               and not any(a in deps for deps in resultados["dependencias_internas"].values())]
    if aislados:
        print("\n ARCHIVOS AISLADOS (sin dependencias):")
        print(", ".join(aislados))