PATRONES_POR_EXTENSION = {
    ".py": {
        "funciones": r"def (\w+)\(([^)]*)\):",
        "clases": r"class (\w+)\s*[\(:]",
        "importaciones": r'^(?:from\s+([\w\.]+)\s+import\s+[\w\.]+|import\s+([\w\.]+)(?:\s*,\s*[\w\.]+)*)',
        "constantes": r"^([A-Z_][A-Z0-9_]*)\s*=\s*.+",
        "variables": r"^(\w+)\s*=\s*.+",
        "interfaces": r"class (\w+)\(.*?Protocol.*?\):",
    },
    ".js": {
        "funciones": r"(?:function\s+(\w+)|const\s+(\w+)\s*=\s*(?:function|\([^)]*\)\s*=>))",
        "clases": r"class\s+(\w+)",
        "importaciones": r"(?:import\s+.+\s+from|require\(\s*['\"])[^'\"]+",
        "constantes": r"(?:const|var)\s+([A-Z_][A-Z0-9_]*)\s*=\s*.+",
        "variables": r"(?:let|var)\s+(\w+)\s*=\s*.+",
        "interfaces": r"interface\s+(\w+)",
        "exportaciones": r"export\s+(default\s+)?(function|class|const|let|var)?\s*\w*"
    },
    ".ts": {
        "funciones": r"(?:function\s+(\w+)|const\s+(\w+)\s*=\s*(?:function|\([^)]*\)\s*=>))",
        "clases": r"class\s+(\w+)",
        "importaciones": r"import\s+.+\s+from\s+['\"][^'\"]+",
        "constantes": r"(?:const|readonly)\s+([A-Z_][A-Z0-9_]*)\s*:\s*.+\s*=\s*.+",
        "variables": r"(?:let|var)\s+(\w+)(?:\s*:\s*\w+)?\s*=\s*.+",
        "interfaces": r"interface\s+(\w+)",
        "exportaciones": r"export\s+(default\s+)?(function|class|const|let|var|interface|type)?\s*\w*"
    },
    ".go": {
        "funciones": r"func\s+(\w+)\s*\(([^)]*)\)",
        "clases": r"type\s+(\w+)\s+struct",
        "importaciones": r"import\s+(?:\([^)]*\)|\"[^\"]+\")",
        "constantes": r"const\s+([A-Z_][A-Z0-9_]*)\s*=?\s*.+",
        "variables": r"var\s+(\w+)\s+[\w\.]+(?:\s*=\s*.+)?",
        "interfaces": r"type\s+(\w+)\s+interface",
        "exportaciones": r"\bfunc\s+[A-Z]\w*|type\s+[A-Z]\w*"
    },
    ".java": {
        "funciones": r"(?:public|private|protected|static|\s)+[\w\<\>\[\]]+\s+(\w+)\s*\([^)]*\)\s*\{?",
        "clases": r"class\s+(\w+)",
        "importaciones": r"import\s+[\w\.]+;",
        "constantes": r"(?:public|private|protected|static|\s)*\s*final\s+[\w\<\>\[\]]+\s+([A-Z_][A-Z0-9_]*)\s*=\s*.+",
        "variables": r"(?:public|private|protected|static|\s)+[\w\<\>\[\]]+\s+(\w+)\s*=\s*.+;",
        "interfaces": r"interface\s+(\w+)",
        # Java no usa `export`, usa modificadores de acceso
    },
    ".php": {
        "funciones": r"function\s+(\w+)\s*\(([^)]*)\)",
        "clases": r"class\s+(\w+)",
        "importaciones": r"(?:require|include|use)\s+['\"][^'\"]+['\"]",
        "constantes": r"(?:const|define\s*\(\s*['\"])([A-Z_][A-Z0-9_]*)",
        "variables": r"\$(\w+)\s*=\s*.+",
        "interfaces": r"interface\s+(\w+)",
        # No hay export explícito en PHP
    },
    ".rb": {
        "funciones": r"def\s+(\w+)",
        "clases": r"class\s+(\w+)",
        "importaciones": r"(?:require|include|require_relative)\s+['\"][^'\"]+['\"]",
        "constantes": r"([A-Z][A-Z0-9_]*)\s*=\s*.+",
        "variables": r"(?:@{1,2}|\$)(\w+)\s*=\s*.+",
        "módulos": r"module\s+(\w+)",
        # Ruby no usa exportaciones explícitas
    },
    ".cs": {
        "funciones": r"(?:public|private|protected|static|\s)+[\w\<\>\[\]]+\s+(\w+)\s*\([^)]*\)\s*\{?",
        "clases": r"class\s+(\w+)",
        "importaciones": r"using\s+[\w\.]+;",
        "constantes": r"(?:public|private|protected|static|\s)*\s*const\s+[\w\<\>\[\]]+\s+([A-Z_][A-Z0-9_]*)\s*=\s*.+",
        "variables": r"(?:public|private|protected|static|\s)+[\w\<\>\[\]]+\s+(\w+)\s*(?:=\s*.+)?;",
        "interfaces": r"interface\s+I(\w+)",
        # No hay `export` en C#
    },
    ".cpp": {
        "funciones": r"[\w\*\&]+\s+(\w+)\s*\(([^)]*)\)",
        "clases": r"class\s+(\w+)",
        "importaciones": r"#include\s+[<\"]([^>\"]+)[>\"]",
        "constantes": r"(?:const|#define)\s+([A-Z_][A-Z0-9_]*)",
        "variables": r"(?:static\s+)?[\w\*\&]+\s+(\w+)\s*(?:=\s*.+)?;",
        "interfaces": r"(?:class|struct)\s+(\w+).*?\{?\s*virtual",
        # No usa `export`, aunque puede haber con `__declspec(dllexport)` pero es raro
    },
    ".c": {
        "funciones": r"[\w\*\&]+\s+(\w+)\s*\(([^)]*)\)",
        "clases": r"typedef\s+struct\s+(\w+)",
        "importaciones": r"#include\s+[<\"]([^>\"]+)[>\"]",
        "constantes": r"(?:const|#define)\s+([A-Z_][A-Z0-9_]*)",
        "variables": r"(?:static\s+)?[\w\*\&]+\s+(\w+)\s*(?:=\s*.+)?;",
        "estructuras": r"struct\s+(\w+)",
        # Nada de export
    }
}
