"""Ejercicio 6 (programa padre). Se comunica con hijo.py por stdin/stdout."""
import os
import subprocess
import sys

ruta_hijo = os.path.join(os.path.dirname(os.path.abspath(__file__)), "hijo.py")

proceso = subprocess.Popen(
    [sys.executable, ruta_hijo],  
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    text=True,
)

salida, _ = proceso.communicate(input="7\n")

print("Respuesta del hijo:")
print(salida)
print(f"Código de salida del hijo: {proceso.returncode}")
