import sqlite3 as sql_bd # Se importara la libreria sqlite3

'''
Realizaremos la conexion a la base de datos SQLite para 
ello se usara la funcion connect(ruta) para conectarse a 
la base de datos e interactuar con ella a traves del objeto
de tipo connect que devuelve la funcion.

Tienes que agregar la ruta relativa desde la carpeta raiz
del proyecto de Python, en este caso la carpeta raiz se
llama "Python" que tenia dos subcarpetas Tarea1, Tarea2 y
Tarea3. Ademas puedes tambien utilizar ruta absoluta aunque
es muy poco recomendable, debido a las incompatibilidades
que se pueden generar.
'''
conexion = sql_bd.connect('Tarea2\\Pruebas\\6 - Pruebas con SQLite\\Realizar consultas\\Chinook_Sqlite.sqlite')

'''
Crearemos un objeto de tipo cursor con la funcion cursor() y 
se configurara dicho objeto para que realize la consulta a 
la base de datos con cursor.execute(consulta)
'''
cursor = conexion.cursor()

cursor.execute('select * from Employee')

'''
Con fetchall() se pedira los resultados de la consulta y 
se almacenaran en una variable
'''
resultado = cursor.fetchall()

''' 
En caso de querer solo un resultado de la consulta se puede
utilizar fetchone(), que hace lo mismo que fetchall() pero
con la diferencia de que solo mostrara un resultado y en caso
de que la consulta tenga varios valores por defecto solo mostrara
el primer resultado de la consulta, es decir, la primera fila de
la tabla resultante de la consulta.
'''
# resultado = cursor.fetchone()

'''
Puedes imprimirlo de manera normal con la variable solamente,
o pasar todos los datos a una tupla, set o lista
'''
print(resultado)
print(tuple(resultado))

conexion.close() # Con la funcion close() se cerrara la conexion, cuando no se necesita la base de datos hay que cerrarla 