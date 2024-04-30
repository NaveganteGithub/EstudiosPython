import sqlite3 as db

# Crear la BBDD
# Abrir una conexion, si no existe la creara

conexion = db.connect("tienda.db")
# conexion = db.connect("tienda.sqlite")

# Obtener un cursor
cursor = conexion.cursor()

# Crear la tabla
cursor.execute("CREATE TABLE IF NOT EXISTS PRODUCTOS (codigo INTEGER PRIMARY KEY, descripcion TEXT, precio REAL)")

# Realizar commit para guardar lo que hay en memoria a la base de datos
conexion.commit()
# conexion.rollback() # Borrar los cambios en memoria

# Cerrar la conexion
conexion.close()
