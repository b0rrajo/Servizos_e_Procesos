import subprocess

ip = input("Introduce una IP: ")

subprocess.run(["ping", ip])
