import sqlite3 as db

conexion = db.connect("../conexion.db")

conexion.execute("update tabla1 set sueldo = 2000 where id = 2")

# Recordemos que para utilizar un execute con parametros se necesitan
# que los parametros se declaren de izquierda a derecha

datos = [(2500, 8),
         (2500, 9)
         ]

conexion.executemany("update tabla1 set sueldo = ? where id = ?", datos)

conexion.execute("REPLACE INTO tabla1 values (10, 'Bruno', 5000)")

conexion.commit()
conexion.close()
