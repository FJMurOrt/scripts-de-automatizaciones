import requests
from datetime import datetime

SERVICIOS = [
    "https://www.google.com",
    "https://www.github.com",
    "https://cloud.google.com",
    "https://www.docker.com",
]

LOG = "health_check.log"


def comprobar_servicio(url):
    try:
        respuesta = requests.get(url, timeout=5)
        if respuesta.status_code == 200:
            return True, respuesta.status_code
        else:
            return False, respuesta.status_code
    except requests.exceptions.RequestException as error:
        return False, str(error)


def comprobar_todos_los_servicios():
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG, "a") as archivo_log:
        for servicio in SERVICIOS:
            servicio_activo, informacion = comprobar_servicio(servicio)

            if servicio_activo:
                mensaje = f"[SERVICIO DISPONIBLE] {servicio} respondió correctamente (código {informacion})"
            else:
                mensaje = f"[SERVICIO NO DISPONIBLE] {servicio} falló: {informacion}"

            print(mensaje)
            archivo_log.write(f"[{fecha}] {mensaje}\n")

comprobar_todos_los_servicios()