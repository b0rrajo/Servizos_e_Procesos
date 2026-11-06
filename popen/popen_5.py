"""Ejercicio 5. Separar salida y errores."""
import subprocess

ENCODING = "cp850"


def ejecutar(comando):
    print(f"\n##### Ejecutando: {comando} #####")
    try:
        proceso = subprocess.Popen(
            comando,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding=ENCODING,
            errors="replace",
        )
    except FileNotFoundError:
        print("No se pudo crear el proceso: el ejecutable no existe.")
        return

    salida, errores = proceso.communicate()

    print("--- Salida estándar ---")
    print(salida if salida else "(vacía)")
    print("--- Salida de error ---")
    print(errores if errores else "(vacía)")
    print(f"Código de salida: {proceso.returncode}")

ejecutar(["ipconfig"])
ejecutar(["cmd", "/c", "comando_inexistente_123"])
ejecutar(["comando_inexistente_123"])
