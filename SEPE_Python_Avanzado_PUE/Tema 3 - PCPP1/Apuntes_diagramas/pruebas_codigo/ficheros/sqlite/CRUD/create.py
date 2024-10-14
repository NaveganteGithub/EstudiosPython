import sqlite3 as db

# Dato float: inf (infinito)
# https://stackoverflow.com/questions/67360775/sql-command-to-insert-inf-nan-and-inf-into-sqlite3-database
# https://note.nkmk.me/en/python-inf-usage/#:~:text=with%20integer%20int-,inf%20(infinity)%20in%20float%20type,NumPy%20library%2C%20are%20described%20later.
# https://docs.python.org/es/3/library/stdtypes.html

conexion = db.connect("../conexion.db")

# Podemos realizar insercciones directas
conexion.execute("insert into tabla1 values (1, 'David', 2000.50)")

# Podemos especificar parametros dentro de una consulta SQL

with open("../recursos/hack.jpg", "rb") as archivo:
    fichero = archivo.read()
    bytes_fichero = bytearray(fichero)
    # Podemos realizar insercciones con parametros con un tupla
    conexion.execute("insert into tabla2 values ('15231561S', 'Española', ?, 1)", (bytes_fichero,))

# Podemos realizar insercciones por columnas
conexion.execute("insert into tabla1 (id, nombre) values (2, 'Daniel')")

# Con executemany podemos realizar insercciones multiples
# https://www.pythonparatodo.com/?p=166
datos = ([3, "Maria", float("inf")],
         [4, "Javier", 7000.50],
         [5, "Ismael", 900.23],
         [6, "Alejandro", 1000.12],
         [7, "Jesus", float("inf")]
         )

conexion.executemany("insert into tabla1 values (?, ?, ?)", datos)

datos = (['43243243A', 'Española', bytes_fichero, 4],
         ['65468412D', 'Española', bytes_fichero, 5],
         ['56489498F', 'Española', bytes_fichero, 6]
         )

conexion.executemany("insert into tabla2 values (?, ?, ?, ?)", datos)

# Podemos realizar scripting SQL

script_sql = """
insert into tabla1(id, nombre) values (8, "Elena");
insert into tabla1(id, nombre) values (9, "Rocio");
insert into tabla1(id, nombre) values (10, "Bruno");
"""

conexion.executescript(script_sql)

conexion.commit()
conexion.close()
