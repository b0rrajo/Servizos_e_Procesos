import subprocess

resultado = subprocess.run(["ipconfig"], capture_output=True, text=True, encoding="cp1252", shell=True)

for linea in resultado.stdout.splitlines():
    if "IPv4" in linea:
        print(linea)
