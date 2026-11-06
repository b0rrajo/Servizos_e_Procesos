"""Ejercicio 4. Capturar la salida de ipconfig."""
import subprocess

proceso = subprocess.Popen(
    ["ipconfig"],
    stdout=subprocess.PIPE,   
    text=True,               
    encoding="cp850",
    errors="replace",
)

salida, _ = proceso.communicate()

print("=== Salida de ipconfig ===")
print(salida)
print(f"Código de salida: {proceso.returncode}")
