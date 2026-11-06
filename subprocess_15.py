import subprocess

with open("configuracion.txt", "w") as f:
    subprocess.run(["ipconfig"], stdout=f)