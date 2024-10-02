import socket

# Creamos el socket
mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    mi_socket.connect((socket.gethostname(), 1234))
except ConnectionRefusedError:
    print("Error al conectarse con el servidor o el servidor ha rechazado la conexion")
    exit(1)

# Recibireos el mensaje
# Dentro especificamos el tamaño del buffer, ten cuidado porque el tamaño de buffer
# puede determinar que el mensaje se reciba por completo o solo una parte
mensaje_bytes = mi_socket.recv(1024)

# El mensaje llegara en bytes por lo que tendremos que decodificar esos bytes
mensaje = mensaje_bytes.decode()

print(mensaje)

mi_socket.shutdown(socket.SHUT_RDWR)

mi_socket.close()
