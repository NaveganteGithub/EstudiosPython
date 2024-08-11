import sqlite3 as db

conexion = db.connect("conexion.db")

sql = ("CREATE TABLE IF NOT EXISTS tabla1 ("
       "id integer primary key autoincrement,"
       "nombre text,"
       "sueldo float"
       ")")

sql2 = ("CREATE TABLE IF NOT EXISTS tabla2 ("
        "dni text primary key,"
        "nacionalidad text,"
        "imagen blob,"
        "persona integer,"
        "foreign key (persona) references tabla1(id)"
        ")")

conexion.execute(sql)
conexion.execute(sql2)

conexion.commit()
conexion.close()
