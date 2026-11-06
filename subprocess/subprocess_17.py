import subprocess
import urllib.parse

# 1. Pide al usuario un término de búsqueda
termino = input("Introduce un término de búsqueda: ")

# Codifica el término de manera segura para la URL
url = f"https://www.google.com/search?q={urllib.parse.quote(termino)}"

# 2. Abre Google con el término utilizando cmd, /c, start
subprocess.run(["cmd", "/c", "start", "", url])
