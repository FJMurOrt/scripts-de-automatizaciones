# Comprobación de estado de servicios (Health Check)

Script en Python que comprueba si una lista de servicios (en este caso URLs públicas) responde correctamente, mostrando el resultado y dejando registro en un log.

## Qué hace

- Hace una petición HTTP a cada servicio de una lista configurable
- Comprueba el código de respuesta (éxito si es 200)
- Registra si cada servicio está disponible o no, junto con el detalle (código o error)
- Guarda el resultado en pantalla y en un log con fecha y hora

## Uso

```bash
python3 health_check.py
```

## Tecnologías

- Python 3
- Librería `requests`
