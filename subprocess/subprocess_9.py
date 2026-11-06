import subprocess

resultado = subprocess.run(["type", "archivo_noexiste.txt"], capture_output = True, text = True, shell=True, encoding="cp1252")
    
print(resultado.stderr)
    
print(resultado.stdout)
