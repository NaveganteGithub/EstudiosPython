"""
CRUD
C -> CREATE - insert into
R -> READ - select
U -> UPDATE - update
D -> DELETE - delete
"""

import sqlite3 as db

# Crear la BBDD
# Abrir una conexion, si no existe la creara

conexion = db.connect("tienda.db")
# conexion = db.connect("tienda.sqlite")

# Obtener un cursor
cursor = conexion.cursor()

################ Insertar datos : C -> CREATE ################
# Insertar un registro
# cursor.execute("insert into PRODUCTOS values (1, 'Pantalla', '89.95')")

# Insertar varios registros

"""productos = [(2, 'Teclado', 29.50),
             (3, 'Raton', 15),
             (4, 'Impresora', 67.50)]
sql = "insert into PRODUCTOS values (?,?,?)"
cursor.executemany(sql, productos)"""

################ Consultar datos : R -> READ ################

# Consultar los campos de la tabla
# https://www.delftstack.com/howto/sqlite/sqlite-get-column-names/
cursor.execute("SELECT name FROM PRAGMA_TABLE_INFO('PRODUCTOS')")
datos = cursor.fetchall()
for item in datos:
    print(item)

# Consultar todos los productos
cursor.execute("Select * from Productos")
# Recojo los resultado obtenidos
productos = cursor.fetchall()
for prod in productos:
    print(prod)

print("--------------------------")

# Consultar los productos con precio inferior a 50
cursor.execute("Select * from Productos where precio < 50")
# Recojo los resultado obtenidos
productos = cursor.fetchall()
for prod in productos:
    print(prod)

print("--------------------------")

# Buscar productos cuya descripcion sea Impresora
parametro = ("Impresora",)
cursor.execute("Select * from Productos where descripcion = ?", parametro)
# Recojo los resultado obtenidos
productos = cursor.fetchall()
for prod in productos:
    print(prod)

print("--------------------------")


# Mostrar todos los productos por precio ascendente
cursor.execute("SELECT * from PRODUCTOS order by precio asc")
resultado = cursor.fetchall()
for fila in resultado:
    print(fila)

print("--------------------------")

# Mostrar todos los productos por precio descendente

cursor.execute("SELECT * from PRODUCTOS order by precio desc")
resultado = cursor.fetchall()
for fila in resultado:
    print(fila)

print("--------------------------")

# Mostrar los productos que comienzan por la letra R

# cursor.execute("SELECT * FROM PRODUCTOS where descripcion like \"R%\"")
parametro = ("R%",)
cursor.execute("SELECT * FROM PRODUCTOS where descripcion like ?", parametro)
resultado = cursor.fetchall()
for fila in resultado:
    print(fila)

print("--------------------------")

# Mostrar los productos que contienen la letra e y valen menos de 50 euros

# cursor.execute("SELECT * from PRODUCTOS where descripcion like '%e%' and precio < 50")
parametro = ("%e%", 50)
cursor.execute("SELECT * from PRODUCTOS where descripcion like ? and precio < ?", parametro)
resultado = cursor.fetchall()
for fila in resultado:
    print(fila)

print("--------------------------")

################ Actualizar datos : U -> UPDATE ################
# Subir un 10% el precio de la impresora
# cursor.execute("UPDATE PRODUCTOS set precio = ((precio * 10) / 100) + precio where descripcion = 'Impresora'")
# cursor.execute("SELECT ((precio * 10) / 100) + precio from Productos where descripcion = 'Impresora'")
"""cursor.execute("SELECT precio * 1.1 from Productos where descripcion = 'Impresora'")
resultado = cursor.fetchone()
print(resultado)

cursor.execute("REPLACE INTO PRODUCTOS VALUES(4, 'Impresora', ?)", resultado)"""

cursor.execute("UPDATE PRODUCTOS set descripcion = upper(descripcion)")

# Poner las descripciones en mayusculas de todos los productos

# Eliminar los productos con precio superior a 50

cursor.execute("DELETE from PRODUCTOS where precio > 50")

conexion.commit()
conexion.close()
