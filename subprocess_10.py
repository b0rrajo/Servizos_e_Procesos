import subprocess

resultado = subprocess.run(["ipconfig"], capture_output=True)
print(resultado.stdout)

resultado = subprocess.run(["ipconfig"], text=True, encoding="cp1252", capture_output=True)
print(resultado.stdout)