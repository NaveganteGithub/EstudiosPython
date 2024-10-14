import socket
import uuid

def get_mac_address():
    mac_num = hex(uuid.getnode()).replace('0x', '').upper()
    mac = '-'.join(mac_num[i: i + 2] for i in range(0, 11, 2))
    return mac

def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

print(f"IP: {get_ip_address()}, MAC: {get_mac_address()}")