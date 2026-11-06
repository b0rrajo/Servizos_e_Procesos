import subprocess

try:
    resultado = subprocess.run(["ping", "-n", "4", "google.com"], timeout=10, capture_output=True, text=True, encoding="cp1252")
except subprocess.TimeoutExpired:
    print("El proceso tardó demasiado")
else:
    print(resultado.stdout)
