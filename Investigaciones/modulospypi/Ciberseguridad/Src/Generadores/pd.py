from itertools import product
from string import ascii_uppercase
import sqlite3

def generador_dni(producto_cartesiano: product):
    
    abecedario = list(ascii_uppercase)
    
    '''No siempre es bueno recargar todo el trabajo 
    a la funcion generadora, deja que esta funcion 
    te devuelva los datos empaquetados y luego procesados
    '''
    for digitos_result in producto_cartesiano:

        identificador_numerico: str = "".join(list(digitos_result))
        replicas: list[str] = [identificador_numerico] * len(abecedario)
        lista_dni: list[tuple] = list(zip(replicas, abecedario))

        yield lista_dni

if __name__ == "__main__":
    
    bd = "Investigaciones\\Ciberseguridad\\Src\\Bases_Datos\\dni.sqlite"
    numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    digitos = product(numeros, repeat=8) # Recomiendo no utilizar en exceso del producto cartesiano
    
    try:

        conexion = sqlite3.connect(bd)
        cursor_conexion = conexion.cursor()

        for set_dni in generador_dni(digitos):
            try:
                cursor_conexion.executemany("insert into DNI (identificador_numerico, letra) values (?,?)", set_dni)
            except sqlite3.IntegrityError:
                pass
            else:
                print(set_dni[0][0] + " insertado")
    
    except sqlite3.OperationalError as error:
        print("ERROR:", error, sep="\n")
    except KeyboardInterrupt:
        print("Operacion interrumpida")
    finally:
        conexion.commit()
        cursor_conexion.close()
        conexion.close()