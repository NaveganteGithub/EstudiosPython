import shelve

"""
c - Create
n - New
r - Read
w - Write
"""

mensaje = "Hola ¿que tal?"

ficheros = shelve.open("./datos_y_pruebas", "n") # BAK DIR DAT

ficheros['default'] = None
ficheros['operador'] = "Samuel"
ficheros['control'] = "Aguila 7"

ficheros.close()


ficheros = shelve.open("./datos_y_pruebas", "r")
print(ficheros['operador'], ficheros['default'])
ficheros.close()
