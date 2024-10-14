import sqlite3 as db
import configparser

# Obtener el objeto config
config = configparser.ConfigParser()

# Leer el archivo
config.read(filenames="config.ini")

# Accedemos a la base de datos con los datos que nos pidan
conexion = db.connect(config['sqlite']['database'])

# Hacemos las operaciones
cursor = conexion.cursor()

cursor.execute("Select * from Productos where precio < 50")
filas = cursor.fetchall()
for fila in filas:
    print(fila)

conexion.close()
