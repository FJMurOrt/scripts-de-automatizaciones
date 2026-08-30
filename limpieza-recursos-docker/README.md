# Limpieza de recursos Docker

Script en Bash que elimina contenedores parados e imágenes sin nombre para liberar espacio, que además deja un registró de lo que se elminó.

## ¿Qué hace?

- Elimina contenedores en estado "exited" con `docker container prune`
- Elimina imágenes sin uso/nombre con `docker image prune`
- Compara el número de contenedores/imágenes antes y después de la limpieza
- Muestra un resumen en pantalla y lo guarda en un log con fecha y hora

## Uso

```bash
./limpieza_docker.sh
```

## Tecnologías

- Bash
- Docker
