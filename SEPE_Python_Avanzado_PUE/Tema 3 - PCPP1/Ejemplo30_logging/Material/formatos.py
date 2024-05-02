import logging

FORMAT = '%(name)s:%(levelname)s:%(asctime)s:%(message)s'

logger = logging.getLogger()

# los mensajes de log vayan a un archivo de log
fichero = logging.FileHandler('archivo.log', mode='w')
formato = logging.Formatter(FORMAT)
fichero.setFormatter(formato)

logger.addHandler(fichero)

#logger.setLevel(logging.CRITICAL)
logger.critical("Mensaje critico")
logger.error("Mensaje error")
logger.warning("Mensaje de aviso")
