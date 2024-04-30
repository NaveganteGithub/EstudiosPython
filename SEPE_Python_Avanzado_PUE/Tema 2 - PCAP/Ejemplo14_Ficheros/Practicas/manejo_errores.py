import errno

try:
    stream = ""
    stream = open("aaaa.txt", "rt")
except IOError as ex:
    print(ex.errno)  # 2
    '''if ex.errno == errno.EACCES:
        print("No tienes permisos para abrir ese fichero")
    elif ex.errno == errno.ENOENT:
        print("Ese arhivo no existe")'''

    # A partir de Python 3.7
    match ex.errno:
        case errno.EACCES:
            print("No tienes permisos para abrir ese fichero")
        case errno.ENOENT:
            print("Ese arhivo no existe")
        case _:   # default
            print("Otro error")
finally:
    if stream != "":
        stream.close()

    '''try:
        stream.close()
    except:
        print("Error al cerrar")'''