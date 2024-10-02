import socket

# Creamos el socket
mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    mi_socket.connect((socket.gethostname(), 1234))
except ConnectionRefusedError:
    print("Error al conectarse con el servidor o el servidor ha rechazado la conexion")
    exit(1)


# Para evitar el problema de definicion del tamaño del buffer
# podemos usar la siguiente logica.
mensaje_completo = ""
while True:
    mensaje_bytes = mi_socket.recv(8)

    if len(mensaje_bytes) <= 0:
        print("El mensaje esta incompleto")
        break

    parte_mensaje = mensaje_bytes.decode()
    mensaje_completo += parte_mensaje

print(mensaje_completo)  # Hola, bienvenido al servidor
