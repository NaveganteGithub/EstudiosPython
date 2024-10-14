import errno
from os import  strerror

# Ejemplo de variable global
num1 = 1

def mi_funcion():
    # Ejemplo de variable local
    num2=2
    #print(list(locals()))

try:
    #mi_funcion()
    # Esta variable al estar fuera de cualquier funcion, es una variable global
    stream = open("aaaa.txt", "rt")
except IOError as ex:
    print(ex.errno)  # 2
    print("Error:",  strerror(ex.errno)) # Error: No such file or directory
    '''if ex.errno == errno.EACCES:
        print("No tienes permisos para abrir ese fichero")
    elif ex.errno == errno.ENOENT:
        print("Ese arhivo no existe")'''

    # A partir de Python 3.7
    match ex.errno:
        case errno.EACCES:
            print("No tienes permisos para abrir ese fichero")
        case errno.ENOENT:
            print("Ese archivo no existe")
        case _:   # default
            print("Otro error")
finally:
    # puedes pintar las variables
    print(list(locals()))
    print(list(globals()))
    # Comprobar si la variable stream se ha creado como variable global
    if "stream" in globals():
        stream.close()

    '''try:
        stream.close()
    except:
        print("Error al cerrar")'''