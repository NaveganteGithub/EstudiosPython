import sqlite3 as sq
import random as ran # as es una palabra reservada que sirve

creacion_y_conexion = sq.connect("C:\\Users\\User\\Documents\\Python\\Tarea2\\Pruebas" +
                                 "\\6 - Pruebas con SQLite\\2 - Crear base de datos\\Mi_base_de_datos_2.sqlite")

creacion_y_conexion.execute("create table prueba_1 (" + 
                            "identificador integer primary key autoincrement," +
                            "texto_prueba text," +
                            "litros real"
                            ")"
                            )

# Creara la tabla con la siguientes indicaciones
creacion_y_conexion.execute("create table prueba_2 (" + 
                            "identificador_1 integer," + # integer permite crear una columna con entero que no tedra limite de tamaño
                            "identificador_2 integer," +
                            "texto_prueba text," +
                            "texto_prueba_2 NVARCHAR(120)," + # NVARCHAR permite definir un texto con un tamaño definido
                            "litros real not null," + # not null es un forma de indicar que la columna no tendra valores vacios
                            # NUMERIC creara una columna con con un valor numerico real o float donde 
                            # sus decimales y enteros tendran un tamaño definido en este caso 
                            # 10 digitos por parte del entero y 2 por la parte del decimal
                            "kilos NUMERIC(10, 2) not null," + 
                            # CONSTRAINT es una instruccion que me permite generar un regla o 
                            # restrincion que me permite determinar como se deben introducir
                            # los datos en la tabla.
                            # Esta es una constraint o regla que indicara que la columna del 
                            # identificador 1 y 2 seran una clave compuesta
                            "CONSTRAINT identificadores_p2 PRIMARY KEY (identificador_1, identificador_2)" +
                            ")"
                            )

creacion_y_conexion.execute("create table prueba_3 (" + 
                            "identificador integer," +
                            "edad integer," +
                            "texto_prueba text," +
                            "identificador_fk text," +
                            "CONSTRAINT clave_primaria_ajena_p3 PRIMARY KEY (" +
                                "identificador,"
                                "edad"
                            "), FOREIGN KEY ("+
                                "identificador_fk" +
                            ") REFERENCES prueba_1 (identificador)"+
                            ")"
                            )

creacion_y_conexion.execute("create table prueba_4 (" + 
                            "identificador integer primary key autoincrement," +
                            "libro text," +
                            # Aqui se esta haciendo una regla para declarar a 
                            # a la columma identificador_fk como clave ajena 
                            # de identificador de la tabla prueba_1
                            # Recuerda que las claves ajenas tienen que tener 
                            # el mismo tipo de dato que la clave primaria a 
                            # la que se va hacer referencia
                            "identificador_fk integer," +
                            "CONSTRAINT clave_ajena_p4 FOREIGN KEY (" + 
                                "identificador_fk" + # nombre de la columna que sera la clave ajena de la tabla prueba_4
                            ") REFERENCES prueba_1 (identificador)" + # nombre_de_la_tabla (nombre_de_la_columna)
                            ")"
                            )

creacion_y_conexion.commit()

print("Tabla creada")
    
creacion_y_conexion.execute("insert into prueba_1 (texto_prueba, litros) values (?, ?)", ('Mi texto 1', 50.21))
creacion_y_conexion.execute("insert into prueba_1 (texto_prueba, litros) values (?, ?)", ('Mi texto 2', 40.81))
creacion_y_conexion.execute("insert into prueba_1 (texto_prueba, litros) values (?, ?)", ('Mi texto 3', 55.84))

creacion_y_conexion.commit()

print("Datos insertados")



cursor = creacion_y_conexion.cursor()
cursor.execute('select * from prueba_1')
resultado = cursor.fetchall()
print(resultado)



creacion_y_conexion.close()
print("Base de datos cerrada")