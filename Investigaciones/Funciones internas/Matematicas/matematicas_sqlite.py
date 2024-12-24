'''
import sqlite3 as db

bd = "Src\\matematicas\\Matematicas.sqlite"

try:
    conexion = db.connect(bd)
    conexion.execute("""
        Create table IF NOT EXISTS Matematicas (
                    id integer primary key autoincrement,
                    Operaciones text unique
        )
    """)
    
except db.OperationalError as error:
    print(error)
finally:
    conexion.close()

try:
    conexion = db.connect(bd)
    conexion.execute("insert into Matematicas (Operaciones) values (?)", ("2 + 2",))
    conexion.commit()
except db.IntegrityError as error:
    print(error)
finally:
    conexion.close()

try:
    conexion = db.connect(bd)
    cursor = conexion.cursor()
    cursor.execute("select Operaciones from Matematicas")
    tabla = cursor.fetchall()
except db.OperationalError as error:
    print(error)
else:
    resultado = eval(tabla[0][0])
    print(resultado)
finally:
    conexion.close()

'''

import sqlite3 as db

bd = "Src\\matematicas\\Matematicas.sqlite"

try:
    conexion = db.connect(bd)
    conexion.execute("""
        Create table IF NOT EXISTS Operacion (
                    id integer primary key autoincrement,
                    Nombre text unique,
                    Descripcion text,
                    Calculo text unique
        )
    """)
    
except db.OperationalError as error:
    print(error)
finally:
    conexion.close()

try:
    conexion = db.connect(bd)
    # conexion.execute("insert into Operacion (Calculo) values (?)", ("2 + 2",))
    conexion.execute("insert into Operacion (Nombre, Descripcion, Calculo) values (?,?,?)", ("Suma de 2", "Sumamos dos más dos", "2 + 2"))
    conexion.commit()
except db.IntegrityError as error:
    print(error)
finally:
    conexion.close()

try:
    conexion = db.connect(bd)
    cursor = conexion.cursor()
    cursor.execute("select Calculo from Operacion")
    tabla = cursor.fetchall()
except db.OperationalError as error:
    print(error)
else:
    resultado = eval(tabla[0][0])
    print(resultado)
finally:
    conexion.close()