from scapy.all import *

"""
https://codigospython.com/manipulacion-de-paquetes-de-red-con-scapy-en-python/
https://www.solvetic.com/tutoriales/article/2659-crear-un-syn-scan-con-python-y-scapy/
https://www.freecodecamp.org/news/how-to-use-scapy-python-networking/
https://www.youtube.com/watch?v=iKW2jx4XNbg
https://vay3t.medium.com/hacking-con-python-3-capitulo-8-entendiendo-scapy-8bf619514d04
https://scapy.readthedocs.io/_/downloads/en/stable/pdf/
https://www.solvetic.com/tutoriales/article/2659-crear-un-syn-scan-con-python-y-scapy/

https://allyring.github.io/picoctf-tftp
https://0xdf.gitlab.io/
https://book.hacktricks.xyz/generic-methodologies-and-resources/exfiltration
https://denizhalil.com/2023/10/17/decrypting-encrypted-network-traffic-python-scapy/
https://scapy.readthedocs.io/en/latest/usage.html#identifying-rogue-dhcp-servers-on-your-lan
https://scapy.readthedocs.io/en/latest/usage.html#asynchronous-sniffing
https://abcdario.org/
"""


"""
payload = "TEST"
send(IP(dst="192.168.1.2")/IP(dst="192.168.1.2")/UDP(dport=4444)/payload)"""

#############################

"""p = IP(dst="github.com")/ICMP()
r = sr1(p)
respuesta = sniff(count=10, prn=lambda x: x.summary())
for i in respuesta:
    print(i.show())"""

#############################

"""p = IP(dst="github.com")/ICMP()
# p[IP].dst = "example.com"  # Cambia la dirección IP de destino
sr1(p)

def process_packet(packet):
    if ICMP in packet:
        packet[ICMP].type = 8  # Cambia el tipo ICMP a Echo Request
        respuesta = sr1(packet, count=5)
        for i in respuesta:
            print(i)

sniff(count=5, filter="icmp", prn=process_packet)"""

#################

"""# Configuras los protocolos
protocolo_ip = IP()
protocolo_ip.dst = "80.58.61.250"

protocolo_icmp = ICMP()
protocolo_icmp.type = 8
protocolo_icmp.code = 0

# Creas el paquete
paquete = protocolo_ip/protocolo_icmp
# Envio el paquete
send(paquete)"""


#########################

"""filtro = ("udp", "tcp") 
paquetes = sniff(filter=filtro[1], count=50)

for paquete in paquetes:
    try:
        for index in range(50):
            layer = paquete[index]
            print(layer)
    except:
        pass"""

#########################

"""# Crear un paquete Scapy (por ejemplo, un paquete Ethernet/IP)
paquete = Ether() / IP() / Raw(load=b"Hola mundo")

# Acceder al campo "load"
raw_data = paquete[Raw].load

# Imprimir el contenido
print(f"Contenido crudo: {raw_data.decode('utf-8')}")"""

##########################

"""# Solo puedes usar o tcp o udp
filtro = ("udp", "tcp", "tcp port 80", "tcp port 443", "tcp port 21") 

paquetes = sniff(filter=filtro[3], # filter nos petmite filtrar paquetes a traves de udp o tcp y un puerto
                 count=1000) # Count nos permite determinar cuantos paquetes tiene que capturar antes de terminar

try:

    for paquete in paquetes:
        paquete.show()
        
        ip_origen = paquete[IP].src
        ip_destino = paquete[IP].dst
        print(ip_origen, "->", ip_destino)
        
        checksum_packet = paquete[TCP].chksum
        print(checksum_packet)

        contenido_raw = raw(paquete)
        contenido_hex = hexdump(paquete)
        
        if Raw in paquete: # Esto es para paquetes con contenido HTML o FTP
            contenido = paquete[Raw].load
            try:
                print("Contenido -", contenido.decode("utf-8"))
            except UnicodeDecodeError:
                pass
                
        print("Raw -", contenido_raw)
        print("Hexadecimal -", contenido_hex)

except IndexError:
    pass"""

###########################

"""# Solo puedes usar o tcp o udp
filtro = ("udp", "tcp", "icmp", "tcp port 80", "tcp port 443", "tcp port 21","host 192.168.1.34") 
paquete = IP(src="192.168.1.34", dst="80.58.61.250")/ICMP()

for _ in range(10):
    paquete.show()
    send(paquete)
    paquete = sniff(filter=filtro[6], count=1)
    print(paquete)
    paquete = IP(src="192.168.1.34", dst="80.58.61.250")/ICMP()
    paquete[IP].type = 8"""


##########################

"""ip_destino = ("80.58.61.250", "8.8.8.8")
filtro = ("udp", "tcp", "icmp", "tcp port 80", "tcp port 443", "tcp port 21","host 192.168.1.34") 
paquete = IP(src="192.168.1.34", dst=ip_destino[1])/ICMP()

for i in range(1, 4):
    send(paquete)
    paquete = sniff(filter=filtro[6], count=1)
    paquete[IP].dst = ip_destino[i % 2]
    paquete.show()"""


########################

"""paquete = IP(src="192.168.1.1", ttl=50)

print(paquete.src)
del paquete.src
print(paquete.src)

print(paquete.ttl)
del paquete.ttl
print(paquete.ttl)

paquete = IP(src="192.168.1.1", ttl=50)/ICMP(id=0x55)

print(paquete[IP].src)
del paquete[IP].src
print(paquete[IP].src)

print(paquete[IP].ttl)
del paquete[IP].ttl
print(paquete[IP].ttl)

print(paquete[ICMP].id)
del paquete[ICMP].id
print(paquete[ICMP].id)"""
