import logging

logging.basicConfig()

logger = logging.getLogger()

logger.critical("Mensaje critico")
logger.error("Mensaje error")
logger.warning("Mensaje de aviso")

logger.setLevel(logging.INFO)
logger.info("Mensaje de informacion")

logger.setLevel(logging.DEBUG)
logger.debug("Mensaje de debug")

logger.setLevel(logging.CRITICAL)
logger.critical("Mensaje critico")

logger.setLevel(logging.ERROR)
logger.error("Mensaje error")

logger.setLevel(logging.WARNING)
logger.warning("Mensaje de aviso")
