import http.client as client
import socket, os, struct, select, time, re

"""
PyClientWeb es un script que pretende ser una version mas simplificada de la libreria
requests, haciendo que el codigo sea legible para que sea facil personalizarlo, 
evitando la utilizacion de librerias externas (Pure Python), y que como requests
sea facil de utilizar.

Fuentes utilizadas:
https://docs.python.org/3/library/http.html#http-status-codes
https://docs.python.org/es/3/library/http.client.html#examples
"""

# -------------- Nivel de enlace o Capa 1 -------------- #
# Aqui dentro trabajaremos con los bytes dentro de nuestra
# red, para empezar, he pensado en una funcion que capture
# los bytes de entrada a la tarjeta de red de nuestro host
def lectura_bytes():
    pass

# -------------- Nivel de enlace o Capa 2 -------------- #

def es_MAC(mac: str):
    delimitadores = mac.count(":") != 5
    contenido = re.match(r"[0-9A-Fa-f\:]+", mac) is None
    campos = len(mac.split(":")) != 6
    # 6 campos x 2 caracteres = 12 caracteres + 5 delimitadores = 17
    longitud = len(mac) != 17 

    if delimitadores or contenido or campos:
        return (False, "No es una mac")
    
    return (True, "Es una mac")

# -------------- Nivel de red/paquete o Capa 3 -------------- #
# IP
def es_IP(ip: str) -> tuple:
    
    lista_blanca = ("::1/128", "::/128", "::ffff:0:0/96")
    
    for ip_permitida in lista_blanca:
        if ip == ip_permitida: return (True, "Es una ip")
    
    if ip.find(".") != -1:
        # Condiciones para IPv4
        limitadores = ip.count(".") != 3
        longitud = len(ip) > 15 # 4 campos x 3 digitos = 12 caracteres + 3 puntos = 15 
        contenido = re.match(r"[0-9.]+", ip) is None
        anomalia = False in [campo.isnumeric() for campo in ip.split(".")] 

        # Si la IP cumple con los requisitos todas las condiciones
        # de este if deberian estar a False
        if limitadores or longitud or contenido or anomalia: \
            return (False, "No es una ip")
        
    elif ip.find(":") != -1 and ip.find(".") == -1:
        # Condiciones para IPv6
        contenido_ip = re.match(r"[0-9a-fA-F\:]+", ip) is None
        principio_ip = re.match(r"^[0-9a-fA-F]+", ip) is None
        # 8 campos x 4 caracteres = 32 caracteres + 7 doble punto = 39
        longitud = len(ip) > 39 
        # mascara_ip = re.match(r"[\/][0-9]{1,3}$", ip) is None
        # contenido_ip_con_mascara = re.match(r"[0-9a-fA-F\:\/]+", ip) is None

        # Si todas las condiciones son False, entonces la IP está correctamente
        if principio_ip or contenido_ip or longitud: \
            return (False, "No es una ip")

    return (True, "Es una ip")
    
class ping():

    def checksum(self, source_string):

        sum = 0
        count_to = (len(source_string) / 2) * 2
        count = 0
        
        while count < count_to:
            this_val = source_string[count + 1] * 256 + source_string[count]
            sum = sum + this_val
            sum = sum & 0xffffffff
            count = count + 2
        if count_to < len(source_string):
            sum = sum + source_string[len(source_string) - 1]
            sum = sum & 0xffffffff
        sum = (sum >> 16) + (sum & 0xffff)
        sum = sum + (sum >> 16)
        answer = ~sum
        answer = answer & 0xffff
        answer = answer >> 8 | (answer << 8 & 0xff00)
        return answer

    def create_socket(self, dest_ip):
        icmp_proto = socket.getprotobyname('icmp')
        try:
            my_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp_proto)
        except socket.error as e:
            if e.errno == 1:
                msg = 'ICMP messages can only be sent from processes running as root.'
                raise socket.error(msg)
            raise
        return my_socket

    def send_ping(self, my_socket, dest_ip, ID):
        dest_addr  =  socket.gethostbyname(dest_ip)
        my_checksum = 0
        header = struct.pack('bbHHh', 8, 0, my_checksum, ID, 1)
        data = struct.pack('d', time.time())
        my_checksum = self.checksum(header + data)
        header = struct.pack('bbHHh', 8, 0, socket.htons(my_checksum), ID, 1)
        packet = header + data
        my_socket.sendto(packet, (dest_addr, 1))

    def do_one_ping(self, dest_ip, timeout):
        icmp = socket.getprotobyname('icmp')
        my_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)
        my_ID = os.getpid() & 0xFFFF
        self.send_ping(my_socket, dest_ip, my_ID)
        delay = self.receive_pong(my_socket, my_ID, timeout)
        my_socket.close()
        return delay

    def receive_pong(self, my_socket, ID, timeout):

        time_left = timeout

        while True:
            started_select = time.time()
            what_ready = select.select([my_socket], [], [], time_left)
            how_long_in_select = (time.time() - started_select)
            if what_ready[0] == []: # Timeout
                return
            time_received = time.time()
            rec_packet, addr = my_socket.recvfrom(1024)
            icmp_header = rec_packet[20:28]
            type, code, checksum, packet_ID, sequence = struct.unpack(
                'bbHHh', icmp_header
            )
            if packet_ID == ID:
                bytes_in_double = struct.calcsize('d')
                time_sent = struct.unpack('d', rec_packet[28:28 + bytes_in_double])[0]
                return time_received - time_sent
            time_left = time_left - how_long_in_select
            if time_left <= 0:
                return

    def ping(self, dest_ip, timeout = 1):
        delay = self.do_one_ping(dest_ip, timeout)
        if delay == None:
            print('Request timed out')
        else:
            delay = delay * 1000
            print('Received ping from %s: icmp_seq=%d time=%.1f ms' % (dest_ip, 1, delay))

# -------------- Nivel de aplicacion o Capa 7 -------------- #

# DNS
def existe_dominio(url: str, verbose_url: bool = False):
    try:
        sock = socket.socket()
        sock.connect((url, 80))
    except socket.error as e:
        return [False, f"No existe el dominio {url}"]
    else:
        sock.close()
        return [True, f"Existe el dominio {url}"]

# HTTP

def get(url: str = "https://www.python.org/", tiempo_espera_limite: int = 7, verbose: bool = False):
    """
    El metodo get() hara una peticion de tipo GET al servidor web, pidiendo no solo el 
    contenido HTML, sino que tambien devuelve informacion del servidor.

    El metodo get(url="https://www.python.org/") devuelve la siguiente informacion en forma de diccionario:
        - 'Domain': 'www.python.org'
        - 'Protocolo': 'https'
        - 'Recurso': '/'
        - 'Respuesta': [200, 'OK']
        - 'RemoteIpAddress': '151.101.132.223'
        - 'RemotePort': 443
        - 'TiempoConexion': 7
        - 'HTMLRaw': Archivo HTML original
        - 'HTMLFormat': Lista de todas las etiquetas HTML del archivo original
    """
    conexion = None
    traza_conexion = dict()

    # Aqui recopilamos la informacion que nos ofrece el parametro URL
    protocolo = url.split(":")[0].lower()
    dominio = url.split("://")[1].split("/")[0]
    ruta_recurso = "/" + "/".join(url.split("://")[1].split("/")[1:])
    
    # Realizamos un Try para controlar las excepciones que surjan durante
    # el establecimiento de la conexion web
    try:
        # Dependiendo del protocolo de la direccion web dada en el parametro url, 
        # se establecera una conexion http o https
        if protocolo == "http":
            conexion = client.HTTPConnection(dominio, timeout=tiempo_espera_limite)
        elif protocolo == "https":
            conexion = client.HTTPSConnection(dominio, timeout=tiempo_espera_limite)
    # En caso de tener alguna excepcion durante el establecimiento de la conexion
    # saltara alguna de estas excepciones dependiendo del caso
    except client.NotConnected:
        print("No se ha podido conectar con el servidor")
    except client.ImproperConnectionState:
        print("No se ha podido conectar con el servidor")
    except client.InvalidURL:
        print("La URL esta alterada")
    except client.BadStatusLine:
        print("Conexion invalida, debido a la respuesta del servidor")
    except client.HTTPException:
        print("Conexion fallida")
    else:
        # En caso de que HABER ENTABLADO LA CONEXIÓN, y tener el modo verbose activado
        # Imprimiremos que se establecido la conexion correctamente
        if verbose:
            print("Conexion establecida, solicitando informacion.")

    # Guardaremos la informacion del servidor
    traza_conexion["Domain"] = conexion.host
    traza_conexion["Protocolo"] = protocolo
    traza_conexion["Recurso"] = ruta_recurso
    
    # Implementamos este try para controlar las excepciones que surgen 
    # por introducir direcciones URL de dominios que no existen.
    try:
        # Aqui realizamos una peticion GET al servidor web para solicitar un recurso
        conexion.request("GET", ruta_recurso, headers={"Host": dominio})
    except socket.gaierror:
        print("El dominio no existe")

        traza_conexion["Domain"] = conexion.host
        traza_conexion["Protocolo"] = protocolo
        traza_conexion["Recurso"] = ruta_recurso
        traza_conexion["Respuesta"] = [404, "Not Found"]
        traza_conexion["RemoteIpAddress"] = None
        traza_conexion["RemotePort"] = None
        traza_conexion["TiempoConexion"] = None
        traza_conexion["HTMLRaw"] = None
        traza_conexion["HTMLFormat"] = None

        conexion.close()

        return traza_conexion
        
    # Aqui pedimos la respuesta de la conexion y la guardamos en una variable
    respuesta = conexion.getresponse()    
    
    # Aqui recopilamos la respuesta del servidor a nuestra peticion GET
    # https://docs.python.org/3/library/http.html#http-status-codes
    traza_conexion["Respuesta"] = [respuesta.status, respuesta.reason]

    socket_servidor_remoto = conexion.sock
    # Si la conexion se establecido correctamente, es decir, 
    # si el estado de la respuesta es OK y tenemos conexion 
    # con el socket pediremos la informacion del servidor
    if respuesta.status < 300 and socket_servidor_remoto is not None:
        socket_servidor_remoto = str(socket_servidor_remoto)
        remote_address = socket_servidor_remoto.split('\'')[-2]
        remote_port = socket_servidor_remoto.split('\'')[-1].split(")")[0].split(", ")[1]
        traza_conexion["RemoteIpAddress"] = remote_address
        traza_conexion["RemotePort"] = int(remote_port)
        traza_conexion["TiempoConexion"] = conexion.timeout
    else:

        traza_conexion["Domain"] = conexion.host
        traza_conexion["Protocolo"] = protocolo
        traza_conexion["Recurso"] = ruta_recurso
        traza_conexion["Respuesta"] = [302, 'Moved Temporarily']
        traza_conexion["RemoteIpAddress"] = None
        traza_conexion["RemotePort"] = None
        traza_conexion["TiempoConexion"] = None
        traza_conexion["HTMLRaw"] = None
        traza_conexion["HTMLFormat"] = None

        conexion.close()

        return traza_conexion
    
    # Aqui imprimimos la respuesta del servidor, si tenemos el modo verbose activado
    if verbose: print(traza_conexion["Respuesta"][0], traza_conexion["Respuesta"][1])
    
    if respuesta.status == 200:
        body = respuesta.read()
        traza_conexion["HTMLRaw"] = body
        traza_conexion["HTMLFormat"] = str(body).split("\n")
        # print(traza_conexion)
    
    conexion.close() # Cerraremos la conexion establecida anteriormente
    
    return traza_conexion

def post(url: str = "https://www.python.org/", tiempo_espera_limite: int = 7, verbose: bool = False):
    pass

def put(url: str = "https://www.python.org/", tiempo_espera_limite: int = 7, verbose: bool = False):
    pass

def post(url: str = "https://www.python.org/", tiempo_espera_limite: int = 7, verbose: bool = False):
    pass


if __name__ == "__main__":

    prueba = 6
    match prueba:
        case 0:
            print(get(url="https://www.python.org"))
            print(get(url="https://docs.python.org/es/3/library/http.client.html"))
            print(get(url="https://codefellows.github.io/sea-python-401d4/lectures/sockets.html"))
        case 1:
            print(es_IP("127.0.0.1"))
            print(es_IP("151.101.132.223"))
            print(es_IP("151.101.1a2.223"))
            print(es_IP("151.101.132.223."))
            print(es_IP(".151.101.132.223"))
            print(es_IP("2001:0DB8::1428:57ab"))
            print(es_IP("2001:0db8:85a3:0000:1319:8a2e:0370:7344"))
            print(es_IP("2001:0db8:85a3::1319:8a2e:0370:7344"))
            print(es_IP(":2001:0db8:85a3::1319:8a2e:0370:7344"))
            print(es_IP("::1/128"))
            print(es_IP("fe80::/10"))
            print(es_IP("fc00::/7"))
            print(es_IP("ff00::/8"))
            print(es_IP("::ffff:0:0/96"))
            print(es_IP("2001:0DB8::1428:57AB/96"))
        case 2:
            print(es_MAC("00:0F:20:CF:8B:42"))
        case 3:
            print(existe_dominio("tryhackme.com"))
            print(existe_dominio("index.google.com"))
            print(existe_dominio("video.google.com"))
        case 4:
            icmp = ping()
            icmp.ping('127.0.0.1')
            icmp.ping('10.10.140.204')
        case 5:
            descarga = get(url="https://0xdf.gitlab.io/")['HTMLRaw']
        case 6:
            print(get(url='https://opensofty.com/es/2020/5/5/25-mejores-temas-de-iconos-para-ubuntu-y-otros-linux/'))
        case _:
            """
            # Seria buena idea que la libreria antes de poder ejecutarse lanzarse una excepcion
            # cuando no ubiera una conexion estable por X interfaz
            """
            pass
        
    