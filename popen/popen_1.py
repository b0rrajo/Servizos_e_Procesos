import subprocess

proceso = subprocess.Popen(["ping", "127.0.0.1", "-n", "4"])

print(f"PID del proceso: {proceso.pid}")
print("Esperando a que termine el proceso")

codigo = proceso.wait()

print(f"Código de salida devuelto por wait(): {codigo}")
