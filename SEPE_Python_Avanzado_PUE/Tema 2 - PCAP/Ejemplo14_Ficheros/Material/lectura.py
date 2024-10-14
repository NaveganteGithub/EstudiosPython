# Abrir el fichero en modo lectura
# ruta absoluta
#fichero = open("/Users/anaisabelvegascaceres/Desktop/fichero.txt", "rt", encoding="utf-8")

# ruta relativa
fichero = open("fichero.txt", "rt", encoding="utf-8")

# leer todo el contenido del fichero
texto = fichero.read()
print(texto)
print(type(texto))  # <class 'str'>

lineas = texto.splitlines()
print(lineas)

# mover el cursor al inicio
fichero.seek(0)

# leer todo el contenido pero me lo devuelve como una lista
lineas = fichero.readlines()
print(lineas)
print(type(lineas))   # <class 'list'>

# crear una lista con el contenido leido
fichero.seek(0)
lista = list(fichero)
print(lista)

# cerrar el fichero
fichero.close()