import subprocess

proceso = subprocess.Popen(["ping", "127.0.0.1", "-n", "5"])

print(f"poll() inmediatamente después de crear el proceso: {proceso.poll()}")

codigo = proceso.wait()
print(f"wait() ha devuelto: {codigo}")

print(f"poll() después de wait(): {proceso.poll()}")

print(f"returncode: {proceso.returncode}")
