#!/bin/bash

LOG="monitorizacion_detalles.log"
FECHA=$(date '+%Y-%m-%d %H:%M:%S')

USADO=$(df -h / | awk 'NR==2 {print $5}' | tr -d '%')
LIMITE=${1:-80}

if [ "$USADO" -ge "$LIMITE" ]; then
    MENSAJE="El espacio usado está en el $USADO%, por encima del límite del $LIMITE%"
else
    MENSAJE="Espacio usado por debajo del límite permitido ($USADO%)"
fi

echo "$MENSAJE"
echo "[$FECHA] $MENSAJE" >> "$LOG"