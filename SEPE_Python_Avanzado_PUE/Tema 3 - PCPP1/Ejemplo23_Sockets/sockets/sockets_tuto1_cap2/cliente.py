import socket


LONGITUDENCABEZADO = 10 # Esto es parte del encabezado

# Creamos el socket
mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    mi_socket.connect((socket.gethostname(), 1234))
except ConnectionRefusedError:
    print("Error al conectarse con el servidor o el servidor ha rechazado la conexion")
    exit(1)

while True:

    mensaje = ""
    nuevo_mensaje = True # Esto es parte del encabezado
    longitud_mensaje = 0

    while True:
        paquete_bytes = mi_socket.recv(16)  # Recibiremos una parte del mensaje en bytes (que son caracteres)

        # Averiguamos si la parte del mensaje recibida es de un nuevo mensaje o de un mensaje que ya se esta procesando
        if nuevo_mensaje:
            # Analizamos el nuevo tamaño del nuevo mensaje, para ello se extrae la cabecera de la primera parte
            # del nuevo mensaje que se esta procesando, en el primer ciclo del bucle
            print(f"Nueva longitud del mensaje: {paquete_bytes[:LONGITUDENCABEZADO]}")
            longitud_mensaje = int(paquete_bytes[:LONGITUDENCABEZADO])
            print(longitud_mensaje)
            nuevo_mensaje = False  # Declaramos en la cabecera que el mensaje actual ya no es nuevo

        """
        Como recibiremos el mensaje por partes necesitaremos reunir 
        todos los trozos del mensaje a en una misma variable
        """
        mensaje += paquete_bytes.decode() # Decodificaremos la parte del mensaje recibida

        """
        Aqui habremos recibido el mensaje escrito del servidor junto con la cabecera, por lo que "quitaremos" la cabera
        del mensaje y averiguaremos si la longitud del mensaje
        """
        # print(len(mensaje) - LONGITUDENCABEZADO == longitud_mensaje)
        if len(mensaje) - LONGITUDENCABEZADO == longitud_mensaje:
            print("El mensaje ha sido completado")
            print(paquete_bytes[LONGITUDENCABEZADO:])
            print(mensaje)
            nuevo_mensaje = True
            mensaje = ""


"""
Nueva longitud del mensaje: b'28        '
28
El mensaje ha sido completado
b''
28        Hola, bienvenido al servidor
Nueva longitud del mensaje: b'31        '
31
El mensaje ha sido completado
b''
31        El tiempo es 1728225711.9583094
Nueva longitud del mensaje: b'30        '
30
El mensaje ha sido completado
b''
30        El tiempo es 1728225714.958713
Nueva longitud del mensaje: b'31        '
31
El mensaje ha sido completado
b''
31        El tiempo es 1728225717.9595068
Nueva longitud del mensaje: b'31        '
31
El mensaje ha sido completado
b''
31        El tiempo es 1728225720.9598732
"""