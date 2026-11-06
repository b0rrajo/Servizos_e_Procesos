import subprocess

resultado = subprocess.run(["ipconfig"], capture_output=True, text=True, encoding="cp1252", shell=True)
print(resultado.stdout)
