import mysql.connector as libmysql # pip install mysql-connector-python

conexion = libmysql.connect(
    host="localhost",
    user="root",
    password="",
    database="cetelem"
)

# Obtener el cursor
mycursor = conexion.cursor()

# Mostrar las tablas que tengo en esa BBDD
mycursor.execute("SHOW TABLES")
for x in mycursor:
  print(x)

# Consultar todos los productos
mycursor.execute("select * from PRODUCTOS")
productos = mycursor.fetchall()
for prod in productos:
    print(prod)
print("-------------")

# Cerrar la conexion
conexion.close()

