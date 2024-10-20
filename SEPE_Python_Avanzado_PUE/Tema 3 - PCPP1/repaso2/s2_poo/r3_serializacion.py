import shelve

fichero = shelve.open("./mis_datos", "n")

fichero['DEFAULT'] = {1,5,6,8,52}
fichero['opcion1'] = {4,5,8,9,2}

fichero.close()

fichero = shelve.open("mis_datos", "r")
print(fichero['opcion1'])
fichero.close()