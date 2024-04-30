import pymysql

# Configura los detalles de la conexión
host = 'estudiaenpython.zapto.org'
user = ('root')
password = 'muertemuerte'
database = 'information_schema'
port= 3306

# Establece la conexión
try:
    conn = pymysql.connect(host=host, port=port, user=user, passwd=password, db=database)
    mycursor = conn.cursor()
    mycursor.execute("SHOW FULL TABLES FROM information_schema")
    productos = mycursor.fetchall()
    for prod in productos:
        print(prod)
    print("-------------")
    mycursor.close()
except pymysql.Error as e:
    print(f"Error al conectar a la base de datos: {e}")