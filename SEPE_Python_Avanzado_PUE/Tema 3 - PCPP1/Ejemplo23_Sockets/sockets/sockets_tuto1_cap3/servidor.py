import socket, pickle

# Determinamos el tamaño del encabezado del mensaje
LONGITUDENCABEZADO = 10

# Creamos el socket
mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

datos_red = tuple([socket.gethostname(), # IP
                   1237 # PUERTO
                   ])

mi_socket.bind(datos_red)  # Declaramos que este socket es de un servidor
mi_socket.listen(5)  # Haremos que el servidor escuche

# Creamos un flujo de mensaje continuo (stream) para enviar mensajes de manera continua e initerrumpida
while True:
    socket_cliente, direccion_ip = mi_socket.accept()
    print(f"Conexion desde {direccion_ip} a sido establecida con exito.")

    # Para este ejemplo vamos enviar objetos serializados por la red, en este caso vamos a
    # usar un diccionario pero podemos usar objetos JSON, pues se puede serializar cualquier
    # objeto
    diccionario = {1: "Hey", 2: "There"}
    mensaje = pickle.dumps(diccionario)
    paquete = bytes(f'{len(mensaje):<{LONGITUDENCABEZADO}}', "utf-8") + mensaje # Declaramos la cabecera junto con el mensaje

    socket_cliente.send(paquete)
