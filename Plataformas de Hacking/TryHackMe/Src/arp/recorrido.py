
ip = "192.168.x.x"
# ip = "192.168.1.x"
# ip = "192.x.x.x"

ip_list = ip.split(".")
numero_de_x = ip.count("x")

listado_ips = set()

def IP_RED(num_redes: int = 2, verbose: bool = True):

    numero_IP = 254 ** num_redes
    ip_actual = 0
    red_actual = 1

    campos = 2 if num_redes == 2 else 4 - num_redes

    for i in range(1, numero_IP + 1):
        ip_actual = ip_actual + 1
        if i % 255 == 0:
            ip_actual = 1
            red_actual = red_actual + 1
        
        listado_ips.add(".".join(ip_list[:campos]) + "." + str(red_actual) + "." + str(ip_actual))
    
    if verbose:
        print("Correcto" if numero_IP == len(listado_ips) else "Faltan IPs", numero_IP, len(listado_ips))

if numero_de_x == 1:
    
    ip_actual = 0

    for i in range(1, 255):
        ip_actual = ip_actual + 1
        if i % 255 == 0:
            ip_actual = 1
        listado_ips.add(".".join(ip_list[:3]) + "." + str(ip_actual))

    # print("Correcto" if len(listado_ips) == 254 else "Faltan IPs")

elif numero_de_x >= 2:
    IP_RED(numero_de_x)

# print("\n".join(listado_ips))