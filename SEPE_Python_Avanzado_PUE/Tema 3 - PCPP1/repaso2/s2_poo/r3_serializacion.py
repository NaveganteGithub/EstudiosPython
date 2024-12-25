import shelve

# La serialización es el proceso de transformar un objeto en una cadena binaria
# La deserialización es el proceso de transformar una cadena binaria en un objeto

# Permisos de la libreria shelve
# r - READ
# w - WRITE
# c - CREATING (DEFAULT) - Utiliza la existente, si no existe la creá
# n - NEW - Siempre crea la base de datos vacia

fichero = shelve.open("./mis_datos", "n")

fichero['DEFAULT'] = {1,5,6,8,52}
fichero['opcion1'] = {4,5,8,9,2}

fichero.close()  # Output: DIR, DAT, BAK

fichero = shelve.open("mis_datos", "r")
print(fichero['opcion1'])
fichero.close()
