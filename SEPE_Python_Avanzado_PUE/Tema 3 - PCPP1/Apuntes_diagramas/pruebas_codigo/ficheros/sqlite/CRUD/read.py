import sqlite3 as db

conexion = db.connect("../conexion.db")

mi_cursor = conexion.cursor()

resultado = mi_cursor.execute("select * from tabla1")

procesado = resultado.fetchall()

print(procesado)

mi_cursor.close()
conexion.close()
