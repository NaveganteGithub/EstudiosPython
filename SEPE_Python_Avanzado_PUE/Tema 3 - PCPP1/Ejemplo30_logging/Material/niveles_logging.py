import logging

# Obtenemos la configuracion por defecto
#logging.basicConfig()

# Podemos cambiar la configuracion:
# Indicando el archivo de log donde guardar los mensajes
# Estableciendo el nivel de logging
# Creando un formato para los mensajes

#logging.basicConfig(filename='mi_archivo.log', level=logging.DEBUG, format='[%(asctime)s] %(levelname)s - %(message)s')
#logging.basicConfig( level=logging.DEBUG, format='[%(asctime)s] %(levelname)s - %(message)s')
#logging.basicConfig(format='[%(asctime)s] %(levelname)s - %(message)s', level=logging.DEBUG)
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)

logger = logging.getLogger()

logger.critical("Mensaje critico")
logger.error("Mensaje error")
logger.warning("Mensaje de aviso")

logger.setLevel(logging.INFO)
logger.info("Mensaje de informacion")

logger.setLevel(logging.DEBUG)
logger.debug("Mensaje de debug")