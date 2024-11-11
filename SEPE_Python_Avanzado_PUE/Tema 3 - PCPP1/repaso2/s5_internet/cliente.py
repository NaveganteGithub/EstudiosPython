import socket


LONGITUDMENSAJE = 10

mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

datos_red = tuple([socket.gethostname(), 50307])

try:
    mi_socket.connect(datos_red)
except ConnectionRefusedError:
    exit(2)

mensaje = ""


while True:

    es_nuevo = True
    longitud_cabecera = None

    while True:

        recibir_paquete = mi_socket.recv(16)

        if es_nuevo:
            longitud_cabecera = int(recibir_paquete[:LONGITUDMENSAJE])
            es_nuevo = False

        mensaje += recibir_paquete.decode("utf-8")

        if len(mensaje) - LONGITUDMENSAJE == longitud_cabecera:
            print(mensaje)
            es_nuevo = False
            longitud_cabecera = None

