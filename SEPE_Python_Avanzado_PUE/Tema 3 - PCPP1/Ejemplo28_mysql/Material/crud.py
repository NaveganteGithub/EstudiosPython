# pip install mysql-connector-python
import mysql.connector

# Datos de conexion
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="cetelem"
)

# Obtener el cursor
mycursor = mydb.cursor()

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
mydb.close()