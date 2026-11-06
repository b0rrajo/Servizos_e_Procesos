import subprocess

comando = ["systeminfo"]
palabras_clave = [
    "Nombre del sistema", 
    "Memoria física total", 
    "Versión del sistema operativo"
]

try:
    resultado = subprocess.run(
        comando,
        capture_output=True,
        text=True,
        timeout=15,
        encoding="cp850"
    )
    
    print("--- Información del Sistema Filtrada ---")
    for linea in resultado.stdout.splitlines():
        if any(palabra in linea for palabra in palabras_clave):
            print(linea.strip())

except subprocess.TimeoutExpired:
    print("Aviso: El comando 'systeminfo' ha tardado demasiado tiempo en ejecutarse y ha sido cancelado.")
except Exception as e:
    print(f"Ocurrió un error durante la ejecución: {e}")