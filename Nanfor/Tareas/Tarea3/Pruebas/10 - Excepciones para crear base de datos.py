import sqlite3 as sq

creacion_y_conexion = sq.connect("C:\\Users\\User\\Documents\\Python\\Tarea2\\Pruebas" +
                                 "\\6 - Pruebas con SQLite\\2 - Crear base de datos\\Mi_base_de_datos.sqlite")

try: 
    creacion_y_conexion.execute("create table prueba_1 (" + 
                                "identificador integer primary key autoincrement," +
                                "texto_prueba text," +
                                "litros real"
                                ")"
                                )
    
    creacion_y_conexion.commit()
    
    print("Tabla creada")
    
except sq.OperationalError: # esta es una excepcion que salta cuando se ha producido un error en una operacion SQL
    print("Tabla ya estaba creada")

    
try:
    
    creacion_y_conexion.execute("insert into prueba_1 (texto_prueba, litros) values (?, ?)", ('Mi texto 1', 50.21))
    creacion_y_conexion.execute("insert into prueba_1 (texto_prueba, litros) values (?, ?)", ('Mi texto 2', 40.81))
    creacion_y_conexion.execute("insert into prueba_1 (texto_prueba, litros) values (?, ?)", ('Mi texto 3', 55.84))
    
    creacion_y_conexion.commit()
    
    print("Datos insertados")
    
except sq.OperationalError:
    print("Los datos ya existen")



try:    
    cursor = creacion_y_conexion.cursor()
    cursor.execute('select * from prueba_1')
    resultado = cursor.fetchall()
    print(resultado)
except sq.OperationalError:
    print("Error al consultar")



try:
    creacion_y_conexion.close()
    print("Base de datos cerrada")
except sq.OperationalError:
    print("Error al cerrar")