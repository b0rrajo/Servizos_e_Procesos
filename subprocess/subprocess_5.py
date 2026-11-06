import subprocess

directorio = input("Introduce in directorio: ")

subprocess.run(["powershell", "-Command", "Get-ChildItem", directorio])
