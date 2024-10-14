import logging

registro = logging.getLogger("Niveles de logging")

fichero = logging.FileHandler("archivo.log", "w")

estilo_formato = "%(asctime)s: Gravedad %(levelname)s Mensaje %(message)s Nombre del registro %(name)s"
formato = logging.Formatter(estilo_formato)

fichero.setFormatter(formato)

registro.addHandler(fichero)

registro.setLevel(logging.DEBUG)
registro.info("Hola")
registro.debug("Traza 2321313")
registro.warning("Peligro")
registro.error("ERROR")
registro.critical("ADVERTENCIA")
