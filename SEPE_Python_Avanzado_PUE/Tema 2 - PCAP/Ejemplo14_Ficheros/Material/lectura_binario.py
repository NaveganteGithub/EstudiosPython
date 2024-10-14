''' modulo necesario para ficheros binarios'''
import pickle

# Abrir el fichero binario en modo lectura
#fichero = open("binario.bin", "rb")   tambien funciona
fichero = open("binario.pckl", "rb")
print(type(fichero)) # <class '_io.BufferedReader'>

# leemos el contenido
nombres = pickle.load(fichero)

# mostramos el contenido leido
print(nombres)

# mostramos el tipo de dato y vemos que sigue siendo una lista
print(type(nombres))  # <class 'list'>

# cerrar el fichero
fichero.close()