"""
• Función asctime:
• convierte un objeto struct_time o una tupla en una cadena.
• Si no se proporciona un argumento a la función asctime, se utilizará el tiempo devuelto por la
función localtime.
"""
import time

timestamp = 1572879180
st = time.gmtime(timestamp)
print(time.asctime(st)) # Mon Nov  4 14:53:00 2019
