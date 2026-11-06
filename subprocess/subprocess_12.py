import subprocess
try:
    subprocess.run(["cmd", "/c", "exit", "1"], check=True)
except subprocess.CalledProcessError as error:
    print("error!: ", error.returncode)
