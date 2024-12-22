import sqlite3 as db

conexion = db.connect("mi_base_datos.db")

mi_cursor = conexion.cursor()

consulta = mi_cursor.execute("SELECT * FROM Clientes")
resultado = consulta.fetchone()
print(resultado)

consulta = mi_cursor.execute("SELECT * FROM Clientes")
resultado = consulta.fetchmany(3)
print(resultado)

consulta = mi_cursor.execute("SELECT * FROM Clientes")
resultado = consulta.fetchall()
print(resultado)

conexion.close()
