''' Generar la base de datos y la tabla '''

import sqlite3

# Crear la BBDD
# Abrir una conexion, si no existe la creara
conexion = sqlite3.connect("tienda.db")
#conexion = sqlite3.connect("tienda.sqlite")

# Obtener un cursor
cursor = conexion.cursor()

# crear la tabla
cursor.execute("CREATE TABLE IF NOT EXISTS PRODUCTOS  (codigo INTEGER PRIMARY KEY, descripcion TEXT, precio REAL)")

# IMPORTANTE EL COMMIT
conexion.commit()

# cerrar la conexion
conexion.close()