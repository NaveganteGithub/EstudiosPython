import shelve

# r - READ
# w - WRITE
# c - CREATING (DEFAULT) - Utiliza la existente, sino existe la crea
# n - NEW - Siempre crea la base de datos vacia

fichero = shelve.open("./mis_datos", "n")

fichero['DEFAULT'] = {1,5,6,8,52}
fichero['opcion1'] = {4,5,8,9,2}

fichero.close()  # Output: DIR, DAT, BAK

fichero = shelve.open("mis_datos", "r")
print(fichero['opcion1'])
fichero.close()