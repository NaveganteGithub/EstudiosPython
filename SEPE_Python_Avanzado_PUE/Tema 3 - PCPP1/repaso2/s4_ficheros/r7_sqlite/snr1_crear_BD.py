import sqlite3 as bd

conexion = bd.connect("mi_base_datos.db")

tabla_sql = ("CREATE TABLE Clientes ( "
         "Email VARCHAR(100) PRIMARY KEY NOT NULL, "
         "Nombre VARCHAR(100) NOT NULL, "
         "Telefono INT NOT NULL"
         ")")

conexion.execute(tabla_sql)

conexion.commit()

conexion.close()
