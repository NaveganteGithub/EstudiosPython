# Importamos los módulos necesarios.
import socket
import os
import struct
import select
import time

# Esta función calcula y devuelve el checksum de una cadena de bytes.
def checksum(source_string):
    sum = 0
    count_to = (len(source_string) / 2) * 2
    count = 0
    # Sumamos los valores de los bytes en pares.
    while count < count_to:
        this_val = source_string[count + 1] * 256 + source_string[count]
        sum = sum + this_val
        sum = sum & 0xffffffff  # Nos aseguramos de que la suma no exceda los límites de un entero de 32 bits.
        count = count + 2
    # Si la longitud de la cadena es impar, sumamos el último byte.
    if count_to < len(source_string):
        sum = sum + source_string[len(source_string) - 1]
        sum = sum & 0xffffffff  # De nuevo, nos aseguramos de que la suma no exceda los límites de un entero de 32 bits.
    # Calculamos el complemento a uno de la suma.
    sum = (sum >> 16) + (sum & 0xffff)
    sum = sum + (sum >> 16)
    answer = ~sum
    answer = answer & 0xffff
    answer = answer >> 8 | (answer << 8 & 0xff00)
    return answer

# Esta función crea un socket para enviar mensajes ICMP.
def create_socket(dest_ip):
    icmp_proto = socket.getprotobyname('icmp')
    try:
        my_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp_proto)
    except socket.error as e:
        if e.errno == 1:
            msg = 'ICMP messages can only be sent from processes running as root.'
            raise socket.error(msg)
        raise
    return my_socket

# Esta función envía un ping ICMP a la dirección IP de destino.
def send_ping(my_socket, dest_ip, ID):
    dest_addr  =  socket.gethostbyname(dest_ip)
    my_checksum = 0
    # Creamos la cabecera del paquete ICMP.
    header = struct.pack('bbHHh', 8, 0, my_checksum, ID, 1)
    # Creamos los datos del paquete ICMP.
    data = struct.pack('d', time.time())
    # Calculamos el checksum de la cabecera y los datos.
    my_checksum = checksum(header + data)
    # Creamos la cabecera final con el checksum correcto.
    header = struct.pack('bbHHh', 8, 0, socket.htons(my_checksum), ID, 1)
    # Creamos el paquete final.
    packet = header + data
    # Enviamos el paquete.
    my_socket.sendto(packet, (dest_addr, 1))

# Esta función envía un ping y recibe la respuesta.
def do_one_ping(dest_ip, timeout):
    icmp = socket.getprotobyname('icmp')
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)
    my_ID = os.getpid() & 0xFFFF
    send_ping(my_socket, dest_ip, my_ID)
    delay = receive_pong(my_socket, my_ID, timeout)
    my_socket.close()
    return delay

# Esta función recibe la respuesta al ping ICMP.
def receive_pong(my_socket, ID, timeout):
    time_left = timeout
    while True:
        started_select = time.time()
        # Esperamos hasta que haya datos disponibles para leer en el socket o hasta que se agote el tiempo de espera.
        what_ready = select.select([my_socket], [], [], time_left)
        how_long_in_select = (time.time() - started_select)
        if what_ready[0] == []: # Timeout
            return
        time_received = time.time()
        # Leemos el paquete del socket.
        rec_packet, addr = my_socket.recvfrom(1024)
        # Desempaquetamos la cabecera ICMP.
        icmp_header = rec_packet[20:28]
        type, code, checksum, packet_ID, sequence = struct.unpack(
            'bbHHh', icmp_header
        )
        # Si el ID del paquete coincide con el ID que enviamos, calculamos el tiempo de ida y vuelta y lo devolvemos.
        if packet_ID == ID:
            bytes_in_double = struct.calcsize('d')
            time_sent = struct.unpack('d', rec_packet[28:28 + bytes_in_double])[0]
            return time_received - time_sent
        time_left = time_left - how_long_in_select
        if time_left <= 0:
            return

# Esta función envía un ping a la dirección IP de destino y muestra el resultado.
def ping(dest_ip, timeout = 1):
    delay = do_one_ping(dest_ip, timeout)
    if delay == None:
        print('Request timed out')
    else:
        delay = delay * 1000
        print('Received ping from %s: icmp_seq=%d time=%.1f ms' % (dest_ip, 1, delay))

# Llamamos a la función ping con las direcciones IP que queremos comprobar.
ping('127.0.0.1')
ping('10.10.139.112')