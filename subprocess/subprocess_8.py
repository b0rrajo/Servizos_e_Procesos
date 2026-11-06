import subprocess

resultado = subprocess.run(["ipconfig"])
print(resultado.returncode)
if resultado.returncode == 0:
    print("Éxito")
else:
    print("Fracaso")
