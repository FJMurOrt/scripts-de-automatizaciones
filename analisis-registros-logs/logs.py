from collections import Counter

ARCHIVO_DE_LOS_LOGS = "logs.log"
NIVELES_DE_ALERTA = ["ERROR", "WARNING", "INFO"]


def contar_alertar_de_los_logs(archivo):
    contador = Counter()
    try:
        with open(archivo, "r") as f:
            for linea in f:
                for nivel in NIVELES_DE_ALERTA:
                    if nivel in linea:
                        contador[nivel] += 1
                        break
    except FileNotFoundError:
        print(f"Hubo un problema y no se pudo encontrar el archivo '{archivo}'")
        return None
        
    return contador


def resultado_final(contador):
    if contador is None:
        return

    print("Resumen del archivo logs:")
    print()

    total = sum(contador.values())

    for nivel in NIVELES_DE_ALERTA:
        cantidad = contador.get(nivel, 0)
        print(f"{nivel}: {cantidad}")

    print()
    print(f"Total de líneas del archivo de logs: {total}")


contador_resultados = contar_alertar_de_los_logs(ARCHIVO_DE_LOS_LOGS)
resultado_final(contador_resultados)