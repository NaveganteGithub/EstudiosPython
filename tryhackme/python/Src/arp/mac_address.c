#include <Python.h>
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

static PyObject* get_mac_address(PyObject* self, PyObject* args) {
    const char* ip;
    if (!PyArg_ParseTuple(args, "s", &ip)) {
        return NULL;
    }

    int sd;
    struct arpreq areq;
    struct sockaddr_in *sin;
    struct in_addr ipaddr;
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
    // printf("MAC: %s\n", mac);

    return Py_BuildValue("s", mac);
}

static PyMethodDef module_methods[] = {
    {"get_mac_address", get_mac_address, METH_VARARGS, "Get the MAC address for a given IP."},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef module_definition = {
    PyModuleDef_HEAD_INIT,
    "mac_address",
    "A Python module that gets MAC addresses from IP addresses",
    -1, 
    module_methods
};

PyMODINIT_FUNC PyInit_mac_address(void) {
    Py_Initialize();

    return PyModule_Create(&module_definition);
}
