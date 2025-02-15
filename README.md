# 🚖 Taxímetro digital 🚖

Se trata de un prototipo de taxímetro digital que simula y gestiona tarifas de viajes utilizando Python.

## Requisitos previos

Para poder ejecutar el proyecto correctamente necesitarás:

- Python 3.13 o superior.
- Entorno virtual (recomendado para mantener las dependencias separadas).

## Instalación

1. Crea y activa tu entorno virtual:

```bash
python -m venv venv
```

Para activar el entorno:

```bash
#windows
venv\Scripts\activate

#linux/mac
source venv/bin/activate
```

2. Instala las dependencias dentro del entorno virtual:

```bash
pip install -r requirements.txt
```

## Uso

Para iniciar la aplicación, ejecuta el siguiente comando:

```bash
python -m taximeter.cli
```

## Logs

La aplicación genera un archivo de log llamado `taximeter.log` dentro de la carpeta `logs/`. Este archivo contiene información detallada de las actividades realizadas dentro de la aplicación, como el uso de comandos y errores que puedan haber ocurrido.

## Testing

Este proyecto utiliza unittest para las pruebas. Para ejecutar los tests de la aplicación ejecuta:

```bash
python -m unittest discover tests
```

Esto correrá las pruebas contenidas en el directorio `tests/` y mostrará los resultados en la terminal.
