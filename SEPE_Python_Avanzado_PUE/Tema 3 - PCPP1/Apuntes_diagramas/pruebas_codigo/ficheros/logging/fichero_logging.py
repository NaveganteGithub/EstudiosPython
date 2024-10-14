import logging as log

# OPCION 1
# NOTA: con basicConfig, lo que hacemos es agregar una configuracion
# inicial al registro, que despues se puede modificar
log.basicConfig(level=log.WARNING, filename="registro.log", filemode="w")

mi_registro = log.getLogger()

mi_registro.critical("NOT FOUND")
mi_registro.warning("BINARY FILE")

# OPCION 2
mi_registro = log.getLogger()
mi_fichero = log.FileHandler("registro2.log", "w")
mi_registro.addHandler(mi_fichero)

mi_registro.warning("FILE NOT FOUND")
