import sqlite3 as db

conexion = db.connect("../conexion.db")

conexion.execute("delete from tabla1 where id = 5")

conexion.commit()
conexion.close()
