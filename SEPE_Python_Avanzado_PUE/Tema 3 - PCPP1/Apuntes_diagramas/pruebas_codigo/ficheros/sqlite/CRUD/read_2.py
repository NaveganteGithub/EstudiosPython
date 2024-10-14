import sqlite3 as db

conexion = db.connect("../conexion.db")

mi_cursor = conexion.cursor()

resultado = mi_cursor.execute("select * from tabla1")  # Consulta a toda la tabla
procesado = resultado.fetchall()  # Devuelve todas las filas en una lista de tuplas

# Consulta a todas las filas de las columnas id y nombre
resultado_2 = mi_cursor.execute("select id, nombre from tabla1")
procesado_2 = resultado_2.fetchall()

print(procesado)
# [(1, 'David', 2000.5), (2, 'Daniel', None), (3, 'Maria', inf), (4, 'Javier', 7000.5), (5, 'Ismael', 900.23),
# (6, 'Alejandro', 1000.12), (7, 'Jesus', inf), (8, 'Elena', None), (9, 'Rocio', None), (10, 'Bruno', None)]
print(procesado_2)
# [(1, 'David'), (2, 'Daniel'), (3, 'Maria'), (4, 'Javier'), (5, 'Ismael'),
# (6, 'Alejandro'), (7, 'Jesus'), (8, 'Elena'), (9, 'Rocio'), (10, 'Bruno')]

# Podemos filtrar filas

resultado = mi_cursor.execute("select * from tabla1 where sueldo > 1000")
procesado = resultado.fetchall()
print(procesado)
# [(1, 'David', 2000.5), (3, 'Maria', inf), (4, 'Javier', 7000.5), (6, 'Alejandro', 1000.12), (7, 'Jesus', inf)]

resultado = mi_cursor.execute('select * from tabla1 where nombre like "Da%"')
procesado = resultado.fetchall()  # Todas las filas
print(procesado)  # [(1, 'David', 2000.5), (2, 'Daniel', None)]

# https://pynative.com/python-cursor-fetchall-fetchmany-fetchone-to-read-rows-from-table/
resultado = mi_cursor.execute("select * from tabla1 where id = 7")
procesado = resultado.fetchone()  # Una fila
print(procesado)  # (7, 'Jesus', inf)

resultado = mi_cursor.execute("select dni, nacionalidad from tabla2 where dni like '%412%'")
procesado = resultado.fetchmany(5)  # Varias filas. Size es el número maximo de filas que procesaremos de la tabla
print(procesado)  # [('65468412D', 'Española')]

# 9e999 es igual que decir inf
# -9e999 es igual que decir -inf
# https://stackoverflow.com/questions/72113935/how-do-i-select-floating-point-infinity-literals-from-a-sqlite-database
resultado = mi_cursor.execute("select nombre from tabla1 where sueldo = 9e999")
procesado = resultado.fetchmany(2)
print(procesado)  # [('Maria',), ('Jesus',)]

resultado_8 = mi_cursor.execute("select nombre from tabla1 where sueldo < 2500")
procesado_8 = resultado_8.fetchmany(2)

resultado_8 = mi_cursor.execute("select nombre from tabla1 where sueldo < 2500")
procesado_8_2 = resultado_8.fetchall()

print(procesado_8, procesado_8_2, sep="\n")
"""
[('David',), ('Ismael',)]
[('David',), ('Ismael',), ('Alejandro',)]
"""

resultado = mi_cursor.execute("select dni from tabla2 where nacionalidad != 'Española'")
procesado = resultado.fetchall()
print(procesado)  # []

# Podemos realizar operaciones de union partiendo del diagrama de venn
# https://www.linkedin.com/feed/update/urn:li:activity:7222224173266288640/

"""
Estructura basica

tabla1 [clausula join] tabla2 on tabla1.[primary key] = tabla2.[foreign key]
"""

columnas = "tabla1.nombre, tabla1.sueldo, tabla2.dni, tabla2.nacionalidad, tabla2.persona"

# Me dara el conjunto de datos que tengan en común tabla1 y tabla2
resultado = mi_cursor.execute("select " + columnas + " from tabla1 inner join tabla2 on tabla1.id = tabla2.persona")
procesado = resultado.fetchall()
print(procesado)
# [('David', 2000.5, '15231561S', 'Española', 1), ('Javier', 7000.5, '43243243A', 'Española', 4),
# ('Ismael', 900.23, '65468412D', 'Española', 5), ('Alejandro', 1000.12, '56489498F', 'Española', 6)]

# La consulta anterior ES IGUAL a está
resultado = mi_cursor.execute("select " + columnas + " from tabla1, tabla2 where tabla1.id = tabla2.persona")
procesado = resultado.fetchall()
print(procesado)
# [('David', 2000.5, '15231561S', 'Española', 1), ('Javier', 7000.5, '43243243A', 'Española', 4),
# ('Ismael', 900.23, '65468412D', 'Española', 5), ('Alejandro', 1000.12, '56489498F', 'Española', 6)]

# Me dara el conjunto de datos de toda la tabla tabla1 y todos los
# datos que tengan en común tabla1 y tabla2
resultado = mi_cursor.execute("select " + columnas + " from tabla1 left join tabla2 on tabla1.id = tabla2.persona")
procesado = resultado.fetchall()
print(procesado)
# [('David', 2000.5, '15231561S', 'Española', 1), ('Daniel', None, None, None, None), ('Maria', inf, None, None, None),
# ('Javier', 7000.5, '43243243A', 'Española', 4), ('Ismael', 900.23, '65468412D', 'Española', 5),
# ('Alejandro', 1000.12, '56489498F', 'Española', 6), ('Jesus', inf, None, None, None),
# ('Elena', None, None, None, None), ('Rocio', None, None, None, None), ('Bruno', None, None, None, None)]

# Me dara el conjunto de datos de toda la tabla tabla2 y todos los
# datos que tengan en común tabla1 y tabla2
resultado = mi_cursor.execute("select " + columnas + " from tabla1 right join tabla2 on tabla1.id = tabla2.persona")
procesado = resultado.fetchall()
print(procesado)
# [('David', 2000.5, '15231561S', 'Española', 1), ('Javier', 7000.5, '43243243A', 'Española', 4),
# ('Ismael', 900.23, '65468412D', 'Española', 5), ('Alejandro', 1000.12, '56489498F', 'Española', 6)]

# Me dara todos los datos de la tabla 1 y la tabla 2,
# pero también me dara los datos que tengan en comun
# ambas tablas, pero sin redundancias
resultado = mi_cursor.execute("select " + columnas + " from tabla1 full join tabla2 on tabla1.id = tabla2.persona")
procesado = resultado.fetchall()
print(procesado)
# [('David', 2000.5, '15231561S', 'Española', 1), ('Daniel', None, None, None, None), ('Maria', inf, None, None, None),
# ('Javier', 7000.5, '43243243A', 'Española', 4), ('Ismael', 900.23, '65468412D', 'Española', 5),
# ('Alejandro', 1000.12, '56489498F', 'Española', 6), ('Jesus', inf, None, None, None),
# ('Elena', None, None, None, None), ('Rocio', None, None, None, None), ('Bruno', None, None, None, None)]

# Me dara todos los datos de la tabla1 sin ningun dato de la tabla2
resultado = mi_cursor.execute(
    "select " + columnas + " from tabla1 left join tabla2 on tabla1.id = tabla2.persona where tabla2.persona IS NULL")
procesado = resultado.fetchall()
print(procesado)

# Me dara todos los datos de la tabla2 sin ningun dato de la tabla1
resultado = mi_cursor.execute(
    "select " + columnas + " from tabla1 right join tabla2 on tabla1.id = tabla2.persona where tabla1.id IS NULL")
procesado = resultado.fetchall()
print(procesado)

# Me dara todos los datos de la tabla1 y tabla2 pero sin los datos que tengan ambas tablas en comun
resultado = mi_cursor.execute(
    "select " + columnas + " from tabla1 full join tabla2 on tabla1.id = tabla2.persona where tabla1.id IS NULL")
procesado = resultado.fetchall()
print(procesado)

# Alias
resultado_alias = mi_cursor.execute("select t.dni from tabla2 as t where t.dni like '%D%'")
procesado_alias = resultado_alias.fetchall()
print(procesado_alias)

with open("../recursos/resultado.jpg", "wb") as fichero:
    resultado = mi_cursor.execute("select imagen from tabla2 where dni = '65468412D'")
    procesado = resultado.fetchone()  # Devuelve una tupla
    fichero.write(procesado[0])

conexion.close()
