import sqlite3 as db

conexion = db.connect('mi_bd.db')

mi_cursor = conexion.cursor()

consulta = mi_cursor.execute("SELECT * FROM Empleados where id = 1")
resultado = consulta.fetchone()

print(resultado)

consulta = mi_cursor.execute("SELECT * FROM Empleados")
resultado = consulta.fetchall()

print(resultado)

consulta = mi_cursor.execute("SELECT * FROM Empleados where id between 2 and 4")
resultado = consulta.fetchmany(3)

print(resultado)

mi_cursor.close()
conexion.close()
