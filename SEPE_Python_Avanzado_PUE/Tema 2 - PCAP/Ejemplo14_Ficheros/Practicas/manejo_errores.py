import errno

try:
    stream = ""
    stream = open("aaaa.txt", "rt")
except OSError as ex: # IOError es un alias de OSError
    print(ex.errno)  # 2
    '''if ex.errno == errno.EACCES:
        print("No tienes permisos para abrir ese fichero")
    elif ex.errno == errno.ENOENT:
        print("Ese arhivo no existe")'''

    match ex.errno: # A partir de Python 3.7
        case errno.EACCES:
            print("No tienes permisos para abrir ese fichero.")
        case errno.ENOENT:
            print("Ese archivo o directorio no existe.")
        case errno.ENOSPC:
            print("No queda espacio en el dispositivo.")
        case errno.EFBIG:
            print("El archivo es demasiado grande para abrirlo.")
        case errno.EMFILE:
            print("Demasiados archivos abiertos.")
        case errno.EEXIST:
            print("El archivo ya existe de antes.")
        case errno.EISDIR:
            print("Es un directorio.")
        case errno.EBADF:
            print("Numero de archivo incorrecto.")
        case _: # default
            print("Otro error")
finally:
    if stream != "":
        stream.close()

    '''try:
        stream.close()
    except:
        print("Error al cerrar")'''