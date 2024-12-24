import sqlite3
from itertools import product

bd = "Investigaciones\\Ciberseguridad\\Src\\Bases_Datos\\dni.sqlite"

try:

    '''Cuando estuve en la Tesoreria General del Estado, me di cuenta, 
    gracias a la interfaz del panel que se utiliza para pedir citas, 
    que los DNIs pueden estar repetidos en la parte numerica, por lo
    que cambia el paradigma del programa
    '''
    conexion = sqlite3.connect(bd)
    cursor = conexion.cursor()

    cursor.execute("""Create table DNI (
                   identificador_numerico text,
                   letra text,
                   NombApell text,
                   primary key (identificador_numerico, letra)
        )
    """)
    
except sqlite3.OperationalError as error:
    print("ERROR:", error, sep="\n")
except KeyboardInterrupt:
    print("Operacion interrumpida")
finally:
    cursor.close()
    conexion.close()

#################################################

datos = [('00001522', 'A'), ('00001522', 'B'), ('00001522', 'C'), ('00001522', 'D'), 
         ('00001522', 'E'), ('00001522', 'F'), ('00001522', 'G'), ('00001522', 'H'), 
         ('00001522', 'I'), ('00001522', 'J'), ('00001522', 'K'), ('00001522', 'L'), 
         ('00001522', 'M'), ('00001522', 'N'), ('00001522', 'O'), ('00001522', 'P'), 
         ('00001522', 'Q'), ('00001522', 'R'), ('00001522', 'S'), ('00001522', 'T'), 
         ('00001522', 'U'), ('00001522', 'V'), ('00001522', 'W'), ('00001522', 'X'), 
         ('00001522', 'Y'), ('00001522', 'Z')]

try:
    numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    digitos = product(numeros, repeat=8)

    conexion = sqlite3.connect(bd)
    cursor_conexion = conexion.cursor()
    
    # cursor_conexion.executemany("insert into DNI (identificador_numerico, letra) values (?,?)", datos)

except sqlite3.OperationalError as error:
    print("ERROR:", error, sep="\n")
except KeyboardInterrupt:
    print("Operacion interrumpida")
finally:
    conexion.commit()
    cursor_conexion.close()
    conexion.close()