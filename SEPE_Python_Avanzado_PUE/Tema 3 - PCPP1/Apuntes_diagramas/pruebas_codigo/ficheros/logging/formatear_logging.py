import logging as log

# estilo = '%(name)s'  # root
# estilo = '%(levelname)s'  # WARNING
# estilo = '%(asctime)s'  # 2024-08-13 19:25:00,264
# estilo = '%(message)s'  # Peligro
estilo = '%(asctime)s %(levelname)s %(message)s %(name)s'  # 2024-08-13 19:27:10,393 WARNING Peligro root

mi_registro = log.getLogger()
mi_fichero = log.FileHandler("registro3.log", "w")
mi_formato = log.Formatter(estilo)

mi_fichero.setFormatter(mi_formato)
mi_registro.addHandler(mi_fichero)

mi_registro.warning('Peligro')
