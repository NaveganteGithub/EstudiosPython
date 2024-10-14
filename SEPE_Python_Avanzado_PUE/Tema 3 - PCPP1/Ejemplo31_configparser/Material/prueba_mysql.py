# pip install mysql-connector-python
import mysql.connector
import configparser

# Obtener el objeto config
config = configparser.ConfigParser()

# leer el archivo
config.read(filenames="config.ini")

# Datos de conexion
mydb = mysql.connector.connect(
  host=config['mysql']['host'],
  user=config['mysql']['user'],
  password=config['mysql']['password'],
  database=config['mysql']['database']
)

# Obtener el cursor
mycursor = mydb.cursor()

# Consultar todos los productos
mycursor.execute("select * from PRODUCTOS")
productos = mycursor.fetchall()
for prod in productos:
    print(prod)
print("-------------")

# Cerrar la conexion
mydb.close()