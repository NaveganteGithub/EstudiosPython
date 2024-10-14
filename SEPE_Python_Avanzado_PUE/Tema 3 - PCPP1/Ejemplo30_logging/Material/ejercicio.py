# Con una lista de numeros en modo texto "1", colocar "tres"
# parsear a numero entero
# mostrar la suma
# manejo de errores, excepciones
# los errores llevarlos a una archivo de log
import logging

logger = logging.getLogger("nivel_critical")
# Crear manejador para errores (nivel CRITICAL)
logger.setLevel(logging.CRITICAL)
manejador_critical = logging.FileHandler("log_critical.log", mode='a')
manejador_critical.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(manejador_critical)

logger2 = logging.getLogger("nivel_warning")
# Crear manejador para avisos (nivel WARNING)
logger2.setLevel(logging.WARNING)
manejador_aviso = logging.FileHandler('log_warning.log', mode='a')
manejador_aviso.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger2.addHandler(manejador_aviso)


datos = ["1","2","tres","4","5"]
suma = 0
for dato in datos:
    try:
        num = int(dato)
    except Exception as ex:
        print(ex)
        logger.critical(ex)
        logger2.warning(ex)

    else:
        suma += num

print("Suma:", suma)
