import sqlite3 as sq

# Se creara y se conectara a la base de datos sqlite mediante la funcion connect
creacion_y_conexion = sq.connect("C:\\Users\\User\\Documents\\Python\\Tarea2\\Pruebas" +
                                 "\\6 - Pruebas con SQLite\\2 - Crear base de datos\\Mi_base_de_datos.sqlite")

# Se creara la tabla para la base de datos ya creada
creacion_y_conexion.execute("create table prueba_1 (" + 
                            "identificador integer primary key autoincrement," + # Se creara una clave primaria con valor autoincrementado
                            "texto_prueba text," + # Se creara una columna con un texto de tamaño indefinido
                            # Se creara una columna con con un valor numerico real o float donde 
                            # sus decimales y enteros no tendran un tamaño definido
                            "litros real"
                            ")"
                            )

# Se realizara un guardado de los cambios en la base de datos con la funcion commit
creacion_y_conexion.commit()

print("Tabla creada")
    
# Se haran las insercciones de datos
creacion_y_conexion.execute("insert into prueba_1 (texto_prueba, litros) values (?, ?)", ('Mi texto 1', 50.21))
creacion_y_conexion.execute("insert into prueba_1 (texto_prueba, litros) values (?, ?)", ('Mi texto 2', 40.81))
creacion_y_conexion.execute("insert into prueba_1 (texto_prueba, litros) values (?, ?)", ('Mi texto 3', 55.84))

# Se realizara un guardado de las insercciones en la base de datos con la funcion commit
creacion_y_conexion.commit()

print("Datos insertados")

# Se realizara la consulta
cursor = creacion_y_conexion.cursor()
cursor.execute('select * from prueba_1')
resultado = cursor.fetchall()
print(resultado)

# Se cerrara la conexion
creacion_y_conexion.close()
print("Base de datos cerrada")