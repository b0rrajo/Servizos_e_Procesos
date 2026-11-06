import subprocess

try:
    resultado = subprocess.run(["ping", "-n", "4", "google.com"], timeout=10, capture_output=True, text=True, encoding="cp1252")
    if resultado.returncode !=0:
        print(resultado.returncode)        
except subprocess.TimeoutExpired:
    print("Tiempo de espera agotado")
else:
    print(resultado.stdout)
