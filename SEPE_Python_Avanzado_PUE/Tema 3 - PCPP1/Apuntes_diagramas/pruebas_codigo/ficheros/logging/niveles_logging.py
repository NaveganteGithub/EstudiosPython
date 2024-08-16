import logging as log

reg_critico = log.CRITICAL
reg_warning = log.WARNING  # Por defecto
reg_error = log.ERROR
reg_info = log.INFO
reg_debug = log.DEBUG

mi_registro = log.getLogger()

# Warning
log.critical("NOT FOUND")  # Ejecuta
log.warning("Peligro residuos")  # Ejecuta
log.error("ERROR 404")  # Ejecuta
log.info("Atencion")  # No Ejecuta
log.debug("linea 1:2")  # No Ejecuta

# Critical
mi_registro.setLevel(reg_critico)

log.critical("NOT FOUND")  # Ejecuta
log.warning("Peligro residuos")  # No Ejecuta
log.error("ERROR 404")  # No Ejecuta
log.info("Atencion")  # No Ejecuta
log.debug("linea 1:2")  # No Ejecuta

# Error
mi_registro.setLevel(reg_error)
