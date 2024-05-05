import mysql.connector as sql # pip install mysql-connector-python

conexion = sql.connect(
    host="localhost", # Direccion de la maquina
    user="root", # Usuario de la base de datos
    password="B13nv3n1d0 a MySQL", # Contraseña de la base de datos
    database="tienda" # equivalente a USE [DATABASE_NAME] sirve para seleccionar una base de datos
)

# Obtener el cursor
mi_cursor = conexion.cursor()

# Mostrar las tablas que tengo en esa BBDD, 
# con esto determinamos que se pueden lanzar 
# consultas propias de la base de MySQL y no solo SQL
mi_cursor.execute("SHOW TABLES")
tablas = mi_cursor.fetchall()
for x in tablas:
    print(x)

# CRUD
# Consultar todos los productos
def consulta():
    mi_cursor.execute("select * from PRODUCTOS")
    productos = mi_cursor.fetchall()

    for prod in productos:
        print(prod)

    print("-" * 50)

consulta()

# Insertar un producto
mi_cursor.execute("insert into PRODUCTOS values (4, 'Procesador', 450.15)")
consulta()
conexion.commit()

# Actualizar un producto
mi_cursor.execute("update PRODUCTOS set descripcion = 'RAM', precio = 150.45 where Id = 4")
consulta()
conexion.commit()

# Eliminar un producto
mi_cursor.execute("delete from PRODUCTOS where Id = 4")
consulta()
conexion.commit()

# Cerrar la conexion
conexion.close()

"""
('productos',)
(1, 'Pantalla', 80.5)
(2, 'Impresora', 40.15)
(3, 'Raton', 15.14)
--------------------------------------------------
(1, 'Pantalla', 80.5)
(2, 'Impresora', 40.15)
(3, 'Raton', 15.14)
(4, 'Procesador', 450.15)
--------------------------------------------------
(1, 'Pantalla', 80.5)
(2, 'Impresora', 40.15)
(3, 'Raton', 15.14)
(4, 'RAM', 150.45)
--------------------------------------------------
(1, 'Pantalla', 80.5)
(2, 'Impresora', 40.15)
(3, 'Raton', 15.14)
--------------------------------------------------
"""