import sqlite3
import configparser

# Obtener el objeto config
config = configparser.ConfigParser()

# leer el archivo
config.read(filenames="config.ini")

# Abrir una conexion
conexion = sqlite3.connect(config['sqlite']['database'])

# Obtener un cursor
cursor = conexion.cursor()

# Consultar todos los productos
cursor.execute("select * from PRODUCTOS")
productos = cursor.fetchall()
for prod in productos:
    print(prod)
print("-------------")

# cerrar la conexion
conexion.close()
