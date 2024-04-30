'''  CRUD
  C -> Create -> Insert
  R -> Read -> Select
  U -> Update -> Update
  D -> Delete -> Delete
  '''

import sqlite3

# Abrir una conexion
conexion = sqlite3.connect("tienda.db")

# Obtener un cursor
cursor = conexion.cursor()

''' ************** Insertar datos ************  '''
# Insertar un registro
#cursor.execute("insert into PRODUCTOS values (1, 'Pantalla', 89.95)")

# Insertar varios registros a la vez
productos = [(2,'Teclado',29.50), (3,'Raton',15),(4,'Impresora',67.50)]
sql = "insert into PRODUCTOS values (?,?,?)"
#cursor.executemany(sql,productos)


''' ************** Consultar datos ************  '''
# Consultar los campos de la tabla
cursor.execute("SELECT name FROM PRAGMA_TABLE_INFO('PRODUCTOS')")
datos = cursor.fetchall()
for item in datos:
    print(item)

# Consultar todos los productos
cursor.execute("select * from PRODUCTOS")
# Recojo los resultados obtenidos
productos = cursor.fetchall()
for prod in productos:
    print(prod)   # cada registro en una tupla
print("-------------")

# Consultar los productos con precio inferior a 50
cursor.execute("select * from PRODUCTOS where precio < 50")
productos = cursor.fetchall()
for prod in productos:
    print(prod)
print("-------------")

# Buscar productos cuya descripcion sea Impresora
param = ("Impresora",)  # El parametro tiene que ir en una tupla
cursor.execute("select * from PRODUCTOS where descripcion = ?",param)
productos = cursor.fetchall()
for prod in productos:
    print(prod)
print("-------------")

# Mostrar todos los productos ordenados por precio ascendente
cursor.execute("select * from PRODUCTOS ORDER BY precio")
productos = cursor.fetchall()
for prod in productos:
    print(prod)
print("-------------")

# Mostrar todos los productos ordenados por precio descendente
cursor.execute("select * from PRODUCTOS ORDER BY precio DESC")
productos = cursor.fetchall()
for prod in productos:
    print(prod)
print("-------------")

# Mostrar los productos que comienzan por la letra R
param = ("R%",)
cursor.execute("select * from PRODUCTOS where descripcion LIKE ?", param)
productos = cursor.fetchall()
for prod in productos:
    print(prod)
print("-------------")

# Mostrar los productos que contienen la letra e y valen menos de 50 euros
params = ("%e%", 50)
cursor.execute("select * from PRODUCTOS where descripcion LIKE ? and precio < ?", params)
productos = cursor.fetchall()
for prod in productos:
    print(prod)
print("-------------")


''' ************** Modificar datos ************  '''
# subir un 10% el precio de la impresora
'''cursor.execute("select precio from PRODUCTOS where descripcion = 'Impresora' ")
dato = cursor.fetchone()
precio = dato[0]
precio *= 1.1

param = (precio,)
cursor.execute("update PRODUCTOS set precio = ? where descripcion = 'Impresora' ", param)'''

# Poner las descripciones en mayusculas de todos los productos
cursor.execute("update PRODUCTOS set descripcion = upper(descripcion)")


''' ************** Eliminar datos ************  '''
# Eliminar los productos con precio superior a 50
cursor.execute("delete from PRODUCTOS where precio > 50 ")

cursor.execute("select * from PRODUCTOS")
productos = cursor.fetchall()
for prod in productos:
    print(prod)
print("-------------")

# Importante el commit
#conexion.commit()

# Cerrar la conexion
conexion.close()