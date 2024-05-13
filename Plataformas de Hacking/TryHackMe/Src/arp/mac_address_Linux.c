#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/ioctl.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <net/if.h>
#include <netinet/if_ether.h>
#include <netinet/ether.h>
#include <arpa/inet.h>

int main(int argc, char *argv[]) {
    int sd;
    struct arpreq areq;
    struct sockaddr_in *sin;
    struct in_addr ipaddr;
    char *ip = argv[1]; // IP para el que quieres la dirección MAC
    char mac[18];

    // Crea un socket
    sd = socket(AF_INET, SOCK_DGRAM, 0);
    if (sd < 0) {
        perror("socket");
        exit(1);
    }

    // Configura la estructura arpreq
    memset(&areq, 0, sizeof(areq));
    sin = (struct sockaddr_in *) &areq.arp_pa;
    sin->sin_family = AF_INET;

    // Convierte la dirección IP de string a in_addr
    inet_aton(ip, &ipaddr);
    sin->sin_addr = ipaddr;

    sin = (struct sockaddr_in *) &areq.arp_ha;
    sin->sin_family = AF_UNSPEC;

    // Nombre de la interfaz
    strncpy(areq.arp_dev, "eth0", 15);

    // Realiza la petición ARP
    if (ioctl(sd, SIOCGARP, (caddr_t) &areq) == -1) {
        perror("ioctl");
        exit(1);
    }

    // Formatea e imprime la dirección MAC
    sprintf(mac, "%02x:%02x:%02x:%02x:%02x:%02x",
            (unsigned char)areq.arp_ha.sa_data[0],
            (unsigned char)areq.arp_ha.sa_data[1],
            (unsigned char)areq.arp_ha.sa_data[2],
            (unsigned char)areq.arp_ha.sa_data[3],
            (unsigned char)areq.arp_ha.sa_data[4],
            (unsigned char)areq.arp_ha.sa_data[5]);
    printf("MAC: %s\n", mac);

    return 0;
}
