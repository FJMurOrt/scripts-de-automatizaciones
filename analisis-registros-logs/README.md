# Análisis de registros de logs

Script en Python que analiza un archivo de log y genera un resumen del número de líneas dependiendo del tipo de alerta que encuentre.

## ¿Qué hace?

- Lee un archivo de log línea por línea
- Clasifica cada línea según el nivel de alerta que tenga (puede ser de tipo ERROR, WARNING o INFO)
- Genera un resumen con el total de líneas de cada nivel y el total general

## Uso

```bash
python3 logs.py
```

## Tecnologías

- Python 3
- Módulo `collections.Counter`
