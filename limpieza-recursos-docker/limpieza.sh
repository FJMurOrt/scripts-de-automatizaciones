#!/bin/bash

LOG="limpieza_docker.log"
FECHA=$(date '+%Y-%m-%d %H:%M:%S')

if ! command -v docker &> /dev/null; then
    echo "Error: Docker no está instalado o no está disponible." >&2
    exit 1
fi

CONTENEDORES_ANTES_DE_BORRAR=$(docker ps -a -q | wc -l)
IMAGENES_ANTES_DE_BORRAR=$(docker images -q | wc -l)

BORRADO_DE_CONTENEDORES=$(docker container prune -f)
BORRADO_DE_IMAGENES=$(docker image prune -f)

CONTENEDORES_DESPUES_DEL_BORRADO=$(docker ps -a -q | wc -l)
IMAGENES_DESPUES_DEL_BORRADO=$(docker images -q | wc -l)

CONTENEDORES_QUE_SE_BORRARON=$((CONTENEDORES_ANTES_DE_BORRAR - CONTENEDORES_DESPUES_DEL_BORRADO))
IMAGENES_QUE_SE_BORRARON=$((IMAGENES_ANTES_DE_BORRAR - IMAGENES_DESPUES_DEL_BORRADO))

MENSAJE_FINAL="Limpieza automática completada con éxito: $CONTENEDORES_QUE_SE_BORRARON contenedores y $IMAGENES_QUE_SE_BORRARON imágenes eliminadas."

echo "$MENSAJE_FINAL"
echo "[$FECHA] $MENSAJE_FINAL" >> "$LOG"