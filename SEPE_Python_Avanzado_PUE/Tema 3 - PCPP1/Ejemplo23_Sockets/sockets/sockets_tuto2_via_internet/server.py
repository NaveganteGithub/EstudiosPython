import socket

# El script del servidor debe de estar en la maquina del servidor.
#
# Cuando nosotros trabajamos con redes locales es muy sencillo enviar mensajes,
# porque en el script del servidor tenemos que declarar en el metodo bind la IP
# privada del servidor.
#   La IP local seria la 127.0.0.1
#   La IP privada seria la IP estatica que habrias asignado al servidor,
#   o tambien puede ser la IP dinamina de la maquina.
# Y el cliente solamente tendria que apuntar a esa IP.
#
# Pero cuando nosotros trabajamos con redes publicas el paradigma cambia,
# porque la IP privada solo es relevante para las maquinas que estan dentro
# de la misma red privada que la del servidor, por lo que para conectar un
# cliente a un servidor publico necesitamos la IP publica.
#
# Para usar la IP publica de nuestro socket servidor tenemos que poner la direccion IP 0.0.0.0
# y en el socket cliente tenemos que indicar la IP publica del servidor

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(("0.0.0.0", 9999))

servidor.listen(1)

while True:
    cliente, direccion = servidor.accept()
    cliente.send("Hola Cliente!".encode())
    print(cliente.recv(1024).decode())
