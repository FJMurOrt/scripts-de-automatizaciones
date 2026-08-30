# Monitorización del espacio usado

Script en Bash que comprueba el porcentaje de espacio usado en el disco y avisa si supera el límite de uso que le hayamos indicado.

## Qué hace

- Consulta el uso actual de disco con `df`
- Compara el resultado con el límite que está a 80% por defecto.
- Muestra un mensaje en pantalla y lo guarda en un log con fecha y hora

## Uso

```bash
./monitorizacion_espacio.sh          # usa el umbral por defecto (80%)
./monitorizacion_espacio.sh 90       # usa un umbral personalizado (90%)
```

## Tecnologías

- Bash
