import logging as logi

# NIVELES

niveles_mensaje = [logi.INFO, logi.DEBUG, logi.WARNING, logi.ERROR, logi.CRITICAL]

for nivel in niveles_mensaje:
    print(nivel)

# METODOS MENSAJE

logger = logi.getLogger("NombreDelLog")

logger.info("Mensaje informativo")
logger.debug("Mensaje para depurar codigo")
logger.warning("Mensaje de advertencia")
logger.error("Mensaje de error")
logger.critical("Mensaje de peligro")
"""
Mensaje de advertencia
Mensaje de error
Mensaje de peligro
"""

logger.log(niveles_mensaje[0], "Mensaje log orientado a la informacion")
logger.log(niveles_mensaje[2], "Mensaje log para advertir") # Mensaje log para advertir

# Especificar nivel

logger.setLevel(niveles_mensaje[0])
logger.info("Mensaje informativo")
logger.debug("Mensaje para depurar codigo")
logger.warning("Mensaje de advertencia")
logger.error("Mensaje de error")
logger.critical("Mensaje de peligro")


# Archivos de logs

fichero = logi.FileHandler("archivo.log", "w")
logger.addHandler(fichero)

logger.info("Progreso al 10%")


# Formatos para logs en archivos

estilo = "%(levelname)s %(asctime)s %(name)s %(message)s"
formateo = logi.Formatter(estilo)

fichero.setFormatter(formateo)

logger.info("Realizando analisis")
