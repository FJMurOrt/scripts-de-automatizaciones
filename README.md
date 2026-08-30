# Scripts de Automatización (Bash/Python)

Repositorio donde voy guardando y ampliando scripts de automatización en Python y Bash. Algunos que ya he realizado, por ejemplo, son para monitorización, limpieza, comprobación de servicios o análisis de logs. Cada script incluye manejo de errores y el registro de actividad (logs).

## 📂 Scripts

| Script | Lenguaje | Descripción |
|---|---|---|
| [`monitorizacion-espacio-disco`](./monitorizacion-espacio-disco) | Bash | Comprueba el espacio usado en disco y avisa si supera un umbral configurable |
| [`limpieza-recursos-docker`](./limpieza-recursos-docker) | Bash | Elimina contenedores parados e imágenes sin uso, con registro de lo eliminado |
| [`comprobacion-estado-servicios`](./comprobacion-estado-servicios) | Python | Comprueba si una lista de servicios/URLs responde correctamente vía HTTP |
| [`analisis-registros-logs`](./analisis-registros-logs) | Python | Analiza un archivo de log y genera un resumen por nivel de severidad (ERROR, WARNING, INFO) |

## 🛠️ Tecnologías

- Bash
- Python 3
- Docker (sólo para el caso del script de limpieza de recursos que no se usan en docker)

## 🚀 Uso

Cada script se ejecuta de manera independiente. Por ejemplo:

```bash
cd monitorizacion-espacio-disco
./monitorizacion_espacio.sh

cd comprobacion-estado-servicios
python3 health_check.py
```
