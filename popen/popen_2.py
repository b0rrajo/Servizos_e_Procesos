import subprocess
import time

proceso = subprocess.Popen(["ping", "127.0.0.1", "-n", "4"])
print(f"PID del proceso: {proceso.pid}")

while proceso.poll() is None:
    print("El proceso sigue ejecutándose")
    time.sleep(1)

print("Proceso finalizado")
print(f"Código de salida: {proceso.returncode}")
