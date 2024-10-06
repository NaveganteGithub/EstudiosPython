import socket
import pickle

LONGITUDENCABEZADO = 10 # Esto es parte del encabezado

# Creamos el socket
mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    mi_socket.connect((socket.gethostname(), 1237))
except ConnectionRefusedError:
    print("Error al conectarse con el servidor o el servidor ha rechazado la conexion")
    exit(1)

while True:

    mensaje = b""
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

        mensaje += paquete_bytes

        if len(mensaje) - LONGITUDENCABEZADO == longitud_mensaje:
            print("El mensaje ha sido completado")
            print(mensaje[LONGITUDENCABEZADO:])

            diccionario = pickle.loads(mensaje[LONGITUDENCABEZADO:])
            print(diccionario)

            nuevo_mensaje = True
            mensaje = ""

