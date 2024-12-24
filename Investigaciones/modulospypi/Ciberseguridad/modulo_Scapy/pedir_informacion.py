import scapy.all as scapy

p = scapy.Ether()/scapy.IP()/scapy.TCP()
print(p.sprintf("%Ether.src%"))
print(p.sprintf("%IP.src%"))