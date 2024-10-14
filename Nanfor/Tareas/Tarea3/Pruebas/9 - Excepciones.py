
'''
TypeError - salta cuando se aplica un tipo de dato no permitido en una funcion o operacion
ZeroDivisionError - salta cuando intentas dividir por cero
OverflowError - salta cuando el calculo excede el limite para un tipo de dato numerico
IndexError - salta cuando nos pasamos del limite de una secuencia e intentamos acceder a una posicion que no existe
KeyError - salta cuando se intenta acceder a una clave de un diccionario que no existe
FileNotFoundError - salta cuando no se encuentra un archivo en concreto
ImportError - salta cuando hay un error en la importacion, puede ser porque la libreria no exista dentro de tu proyecto
NameError - salta cuando se intenta acceder a un archivo o directorio que no existe
'''

try:
    fichero = open("adsada.txt", "r")
    lectura = fichero.read()
    fichero.close()
    print(fichero)
except NameError:
    print("El archivo no existe")
except FileNotFoundError:
    print("El archivo no existe")
finally:
    print("Proceso finalizado") # Se ejecuta aunque salte la excepcion

print("Proceso finalizado")