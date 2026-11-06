import subprocess

resultado = subprocess.run("echo Hola && dir", shell=True, capture_output=True, text=True, encoding="cp1252")
print (resultado.stdout)