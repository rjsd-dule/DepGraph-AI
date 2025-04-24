import os
import subprocess
import sys
from pathlib import Path
import shutil

# Paso 1: Crear entorno virtual
print(" Creando entorno virtual...")
venv_path = Path("venv")

if not venv_path.exists():
    subprocess.run([sys.executable, "-m", "venv", "venv"])
else:
    print(" Entorno virtual ya existe, se reutilizará.")

# Paso 2: Activar entorno virtual
if os.name == "nt":
    activate_cmd = ".\\venv\\Scripts\\activate.bat"
else:
    activate_cmd = "source ./venv/bin/activate"

# Paso 3: Instalar dependencias
print(" Instalando dependencias desde requirements.txt...")
pip_path = venv_path / ("Scripts" if os.name == "nt" else "bin") / "pip"
subprocess.run([str(pip_path), "install", "--upgrade", "pip"])
subprocess.run([str(pip_path), "install", "-r", "requirements.txt"])

# Paso 4: Configurar .env si no existe
if not Path("config.env").exists():
    if Path("config.env.example").exists():
        shutil.copy("config.env.example", "config.env")
        print(" Archivo config.env creado desde ejemplo.")
    else:
        print(" No se encontró config.env ni config.env.example.")
else:
    print(" Archivo config.env ya existe.")

# Paso 5: Mensaje final
print("\n Proyecto configurado con éxito.")
print(" Activa el entorno con:")
print(f"   {activate_cmd}")
print("Luego ejecuta tu script principal con:")
print("   python main.py")
