import socket

"""
Un socket es lo que se conoce como un "punto final", dentro de una conexion,
tenemos el cliente y el servidor, habitualmente, estos dos, estan conectados
por un canal de comunicacion donde fluyen los mensajes, pues bien, dentro de
este canal de comunicacion (que lo podemos ver como una tuberia de agua), se
puede apreciar que tiene dos extremos, estos son los puntos entrada y salida 
de datos de cualquier transmision de datos que se te ocurra, y eso es lo que
se le conoce como un "punto final".

NOTA: primero crea el socket del servidor y luego el cliente.
"""

# Creamos el socket
mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

"""
En el primer parametro pondriamos la ip de la maquina, pero para no tener 
que estar cambiandola cada rato lo mejor es utilizar gethostname 

En el segundo parametro pondriamos el puerto que usara la maquina, recuerda no usar ningun 
puerto que ya este usando la maquina, pues sino te dara excepcion.

Recomiendo usar puertos dentro de este rango, 49152 – 65535

https://es.wikipedia.org/wiki/Anexo:Puertos_de_red#Puertos_ef%C3%ADmeros
"""

datos_red = tuple([socket.gethostname(), # IP
                   1234 # PUERTO
                   ])
mi_socket.bind(datos_red) # Declaramos que este socket es de un servidor

# Haremos que el servidor escuche, en este caso estamos creando una "cola" para recibir 5 peticiones al mismo tiempo
# para este servidor, 5 peticiones por cada cola, ahora si quisieramos que el servidor pudiera recibir muchas peticiones
# al mismo tiempo, aumentariamos el numero de espacios que tendria la cola. Una cola de 5 posiciones es una cola
# muy pequeña
mi_socket.listen(5)

while True:
    socket_cliente, direccion_ip = mi_socket.accept()
    print(f"Conexion desde {direccion_ip} a sido establecida con exito.")
    """
    Conexion desde ('192.168.56.1', 57507) a sido establecida con exito.
    Conexion desde ('192.168.56.1', 57512) a sido establecida con exito.
    """
    informacion = bytes("Hola, bienvenido al servidor", "utf-8")
    socket_cliente.send(informacion)
    # A nivel muy basico, para transmitir el mensaje completo al cliente
    # hay que cerrar el servidor
    socket_cliente.shutdown(socket.SHUT_RDWR)
    socket_cliente.close()
