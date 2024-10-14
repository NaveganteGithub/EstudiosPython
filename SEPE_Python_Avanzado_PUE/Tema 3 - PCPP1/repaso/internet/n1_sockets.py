import socket

ipv4 = socket.AF_INET
ipv6 = socket.AF_INET6
modo = socket.SOCK_STREAM
aviso = socket.SHUT_RDWR


mi_socket = socket.socket(ipv4, modo)

mi_socket.connect(("www.python.org", 443))

mi_socket.send(b"GET / HTTP1.1\r\nHost: " +
               bytes("www.python.org", "utf-8") +
               b"\r\n Connection: Close \r\n")

resultado = mi_socket.recv(2000)
print(resultado)

mi_socket.shutdown(aviso)

mi_socket.close()
