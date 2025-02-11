# logger.py
import logging
import os

# Crear carpeta 'logs' si no existe y definir ruta del archivo
log_dir = 'logs'
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

log_file = os.path.join(log_dir, 'taximeter.log')

# Configuración básica del logger
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),  # Para guardar en el archivo indicado
    ]
)

# Exportar el logger para usarlo en otros archivos
logger = logging.getLogger('taximeter')
