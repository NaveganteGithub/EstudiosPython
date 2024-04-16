''' modulo necesario para ficheros binarios'''
import pickle

nombres = ['Juan', 'Maria', 'Pedro', 'Pablo', 'Laura']

# abrir el fichero binario en modo escritura
fichero = open("binario.pckl", "wb") # <class '_io.BufferedWriter'>
print(type(fichero))

# escribir el contenido
pickle.dump(nombres, fichero)

# cerrar el fichero
fichero.close()
