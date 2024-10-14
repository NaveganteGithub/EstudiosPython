import socket
import sys
import select
import errno

############## CABECERA ##############

HEADER_LENGHT = 10
IP = "127.0.0.1"
PORT = 1234

######################################

DEBUG = False

mi_nombre_usuario = input("Introduce tu nombre de usuario: ")
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((IP, PORT))

"""
El modo "Bloqueante" es un modo de los sockets de python,
permite forzar la espera del proceso o el hilo para que
metodos como recv o send terminen todas sus operaciones
antes de pasar a la siguiente instruccion.

El modo "No bloqueante" es un modo de los sockets en Python,
que permite que el proceso o el hilo no espere a que metodos
como send o recv terminen sus operaciones, por el contrario,
el programa continuara a pesar de que estos metodos esten en
activo. Importante con este modo si recv() no recibe datos de
manera inmediata el programa puede sufrir un BlockingIOError.

Por defecto el modo Bloqueante esta habilitado pero podemos 
cambiar el socket a modo No bloqueante con la siguiente instruccion. 
"""
cliente.setblocking(False)

# Enviar el nombre del usuario
#

nombre_usuario_enviar = mi_nombre_usuario.encode("utf-8") # Codificamos el nombre de usuario
cabecera_usuario_enviar = f"{len(nombre_usuario_enviar):<{HEADER_LENGHT}}".encode("utf-8")
paquete = cabecera_usuario_enviar + nombre_usuario_enviar
cliente.send(paquete)

# Para evitar que las personas cambien su nombre de usuario
# crearemos un bucle que se ejecute siempre, y que reciba y
# envie mensajes con ese nombre de usuario

while True:
    mensaje = input(f"{mi_nombre_usuario} > ")

    if mensaje:
        mensaje = mensaje.encode("utf-8")
        cabecera_mensaje = f"{len(mensaje):<{HEADER_LENGHT}}".encode("utf-8")
        paquete = cabecera_mensaje + mensaje
        cliente.send(paquete)

    try:
        while True:
            # Recibir cosas
            cabecera_usuario_enviar = cliente.recv(HEADER_LENGHT)

            if not len(cabecera_usuario_enviar):
                print("Conexion cerrada por el servidor")
                sys.exit(0)

            longitud_nombre = int(cabecera_usuario_enviar.decode("utf-8").strip())
            nombre_usuario_enviar = cliente.recv(longitud_nombre).decode("utf-8")

            cabecera_mensaje = cliente.recv(HEADER_LENGHT)
            longitud_nombre = int(cabecera_mensaje.decode("utf-8").strip())
            mensaje = cliente.recv(longitud_nombre).decode("utf-8")

            print(f"{nombre_usuario_enviar} > {mensaje}")

    except IOError as e:

        if DEBUG:
            if e.errno != errno.EAGAIN:
                print("Leyendo error", str(e))
                """
                Leyendo error 
                [WinError 10035] No se puede completar de forma inmediata una operación de desbloqueo de socket
                """

            if e.errno != errno.EWOULDBLOCK:
                print("Leyendo error 2", str(e))

        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            sys.exit(1)

        continue

    except Exception as e:
        print("Error desconocido")
        print("Informacion", str(e))
        sys.exit(1)