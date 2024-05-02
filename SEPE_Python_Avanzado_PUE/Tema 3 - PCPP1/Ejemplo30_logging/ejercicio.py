# Con una lista de numeros en modo texto "1", colocar "tres"
# parsear a numero entero
# mostrar la suma
# manejo de errores, excepciones
# los errores llevarlo a un archivo de log

import logging

lista = ["1", "2", "tres"]
conversion = list()
try:
    for n in lista:
        conversion.append(int(n))
except ValueError as err:

    logging.basicConfig()
    logger = logging.getLogger()

    registro = logging.FileHandler('registro.log', "w")
    logger.addHandler(registro)

    logger.setLevel(logging.ERROR)
    logger.error(err)
else:
    print(sum(conversion))
