import subprocess

ip = input("Introduce la dirección IP o dominio a diagnosticar: ")
comando = ["ping", "-n", "4", ip]

try:
    resultado = subprocess.run(
        comando,
        capture_output=True,
        text=True,
        timeout=10,
        encoding="cp850"
    )
    
    with open("diagnostico.txt", "w", encoding="utf-8") as f:
        f.write(resultado.stdout)
        
    print("\n--- Salida del Diagnóstico ---")
    print(resultado.stdout)
    print(f"Código de salida: {resultado.returncode}")
    print("Diagnóstico completado con éxito. Guardado en 'diagnostico.txt'.")

except subprocess.TimeoutExpired:
    print("Error: El comando ping ha superado el límite de tiempo establecido.")
except Exception as e:
    print(f"Se ha producido un error inesperado: {e}")