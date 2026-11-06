import subprocess
carpeta = input ("Introduce carpeta: ")
try:
    resultado=subprocess.run(["powershell", "-Command", "Get-ChildItem", carpeta], shell=True, capture_output=True, text=True, encoding="cp1252")
    print(resultado.stdout)
except FileNotFoundError as error:
    print("Carpeta no existe", error.returncode)