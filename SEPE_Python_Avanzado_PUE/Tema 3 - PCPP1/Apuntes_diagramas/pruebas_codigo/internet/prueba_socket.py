import socket

modo_internet = socket.AF_INET  # IP version 4
# modo_internet_v6 = socket.AF_INET6  # IP version 6
modo_flujo = socket.SOCK_STREAM

orden_cerrar = socket.SHUT_RDWR

mi_socket = socket.socket(modo_internet, modo_flujo)

mi_socket.connect(("www.python.org", 443))

mi_socket.send(b"GET /doc HTTP/1.1\r\nHost: " +
               bytes("www.python.org", "utf-8") +
               b"\r\nConnection: close \r\n\r\n")

respuesta = mi_socket.recv(20000)

mi_socket.shutdown(orden_cerrar)

mi_socket.close()

print(respuesta.decode())
