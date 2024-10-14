import socket, time

"""
mensaje = "Hola, bienvenido al servidor"
print(f'{len(mensaje):<10}' + mensaje)  # Con los formateos podemos definir espacio en cietas partes de un texto
print(f'{len(mensaje):<20}' + mensaje)
"""

# Determinamos el tamaño del encabezado del mensaje
LONGITUDENCABEZADO = 10

# Creamos el socket
mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

datos_red = tuple([socket.gethostname(), # IP
                   1234 # PUERTO
                   ])

mi_socket.bind(datos_red)  # Declaramos que este socket es de un servidor
mi_socket.listen(5)  # Haremos que el servidor escuche

# Creamos un flujo de mensaje continuo (stream) para enviar mensajes de manera continua e initerrumpida
while True:
    socket_cliente, direccion_ip = mi_socket.accept()
    print(f"Conexion desde {direccion_ip} a sido establecida con exito.")

    mensaje = "Hola, bienvenido al servidor"
    # mensaje = f'{len(mensaje):<10}' + mensaje
    paquete = f'{len(mensaje):<{LONGITUDENCABEZADO}}' + mensaje # Declaramos la cabecera junto con el mensaje

    informacion = bytes(paquete, "utf-8")
    socket_cliente.send(informacion)

    while True:
        time.sleep(3)
        mensaje = f"El tiempo es {time.time()}"
        TIMEHEADER = f"{len(mensaje):<{LONGITUDENCABEZADO}}" + mensaje
        socket_cliente.send(bytes(TIMEHEADER, "utf-8"))
