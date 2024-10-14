import socket


# https://ifconfig.me/
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(("", 9999))

print(cliente.recv(1024).decode())
cliente.send("Hello Server".encode())
