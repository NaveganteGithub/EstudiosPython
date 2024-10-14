# Este script no funciona en Windows, sino en Linux, además, 
# los resultados no son fiables en la primera ejecucion, por
# lo tanto, tendras que ejecutar el script varias veces.
# Otro apunte, tienes que instalar Scapy mediante apt, no lo
# hagas por pip install. Comando: apt install python3-scapy
from scapy.all import *

interface = "ens5"
ip_range = "10.10.43.119/24"
broadcastMac = "ff:ff:ff:ff:ff:ff"

packet = Ether(dst=broadcastMac)/ARP(pdst = ip_range)

ans, unans = srp(packet, timeout =2, iface=interface, inter=0.1)

for send,receive in ans:
        print (receive.sprintf(r"%Ether.src% - %ARP.psrc%"))