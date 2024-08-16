import socket

# Crear el socket

mi_socket = socket.socket(socket.AF_INET,  # Lanzar peticiones a traves de internet
                          socket.SOCK_STREAM  # Recibiremos respuestas de internet
                          )
# socket.SOCK_SEQPACKET # Recibiremos o lanzaremos paquetes
# socket.SOCK_RAW  # Recibiremos o lanzaremos la informacion en crudo

# Conectar al servidor

dominio = "www.python.org"
mi_socket.connect((dominio, 80))  # Ponemos directamente el nombre de dominio, y hay meter los valores en una tupla

# Enviar la peticion

# 1º linea: GET (metodo utilizado) / (indicamos la raiz del server)
#           HTTP:/1.1 Protocolo utilizado \r\n saltos de linea obligatorios
# 2º linea: Host: www.pues.es con juego de caracteres UTF-8  \r\n saltos de linea obligatorios
# 3º linea: Connection: close (cerrar la conexion) \ r\n obligado al final de cada linea
# 4º linea: El metodo obliga a dejar espacios en blanco \r\n

# \r es un salto de linea en Windows
mi_socket.send(b"GET / HTTP/1.1\r\nHost: " +  # Indicaremos el tipo de peticion para el protocolo indicado
               bytes(dominio, "utf8") +  # Indicaremos el host al que vamos a conectarnos
               b"\r\nConnection: close \r\n\r\n"
               )

# Recibir la respuestas
respuestas = mi_socket.recv(20000  # indicamos el tamaño del buffer
                            )
# Antes de cerrar hay que avisar de los motivos del cierre de la conexion
mi_socket.shutdown(socket.SHUT_RDWR)

# Cierre definitivo del socket
mi_socket.close()

# Mostrar la respuesta por consola
print(respuestas.decode())
