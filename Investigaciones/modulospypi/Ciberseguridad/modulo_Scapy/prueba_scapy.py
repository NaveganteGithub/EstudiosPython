from scapy.all import *
import warnings

warnings.filterwarnings("ignore")

packet = IP()/TCP()
print(Ether()/packet)


p = Ether()/IP(dst="www.secdev.org")/TCP()
print(p.summary())

print(p.dst)  # first layer that has an src field, here Ether
print(p[IP].src)  # explicitly access the src field of the IP layer

# sprintf() is a useful method to display fields
print(p.sprintf("%Ether.src% > %Ether.dst%\n%IP.src% > %IP.dst%"))


# Sending and receiving
p = sr1(IP(dst="172.67.27.10")/UDP()/DNS(qd=DNSQR()))
if p:
    print(p[DNS].an)
else:
    pass