import logging as log

# Estructura basica
log.basicConfig()

mi_log = log.getLogger()

mi_log.critical("ERROR 404")  # NIVEL_LOG:nombre_log:Mensaje -- CRITICAL:root:ERROR 404

# Pedir el nivel de log actual

print(mi_log.getEffectiveLevel())
# 30 - > Warning

# NOTA: Primero salen los logs y despues la salida del print()
