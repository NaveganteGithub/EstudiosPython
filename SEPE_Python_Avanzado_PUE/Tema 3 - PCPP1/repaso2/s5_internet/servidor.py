import socket

LONGITUDCABECERA = 10

socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

datos_redes = tuple([socket.gethostname(), 50307])

socket_servidor.bind(datos_redes)
socket_servidor.listen(7)

while True:
    socket_cliente, direccion_cliente = socket_servidor.accept()
    print(f"Se ha conectado el cliente cuya IP es {direccion_cliente}")

    contenido = f"Bienvenido {direccion_cliente}"
    mensaje = f"{len(contenido):<{LONGITUDCABECERA}}" + contenido
    socket_cliente.send(bytes(mensaje, "utf-8"))
