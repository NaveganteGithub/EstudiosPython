#include <iostream>
#include <string>
#include <cstdlib>
#include <cstdio>

#ifdef _WIN32
#include <winsock2.h>
#include <iphlpapi.h>
#pragma comment(lib, "ws2_32.lib")
#pragma comment(lib, "iphlpapi.lib")
#else
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <net/if.h>
#include <netdb.h>
#include <unistd.h>
#endif

std::string getMacAddress(const std::string& ipAddress) {
    std::string macAddress;

#ifdef _WIN32
    IPAddr destIp = inet_addr(ipAddress.c_str());

    ULONG macAddr[2];
    ULONG macAddrLen = 6;

    DWORD dwRetVal = SendARP(destIp, 0, macAddr, &macAddrLen);
    if (dwRetVal == NO_ERROR) {
        char macStr[18];
        snprintf(macStr, sizeof(macStr), "%02X:%02X:%02X:%02X:%02X:%02X",
                 static_cast<unsigned char>(macAddr[0] & 0xFF),
                 static_cast<unsigned char>((macAddr[0] >> 8) & 0xFF),
                 static_cast<unsigned char>((macAddr[0] >> 16) & 0xFF),
                 static_cast<unsigned char>((macAddr[1] >> 0) & 0xFF),
                 static_cast<unsigned char>((macAddr[1] >> 8) & 0xFF),
                 static_cast<unsigned char>((macAddr[1] >> 16) & 0xFF));
        macAddress = macStr;
    }
#else
    int sock = socket(AF_INET, SOCK_DGRAM, 0);
    if (sock == -1) {
        perror("socket");
        return macAddress;
    }

    struct arpreq request;
    memset(&request, 0, sizeof(request));

    struct sockaddr_in* sin = (struct sockaddr_in*) &request.arp_pa;
    sin->sin_family = AF_INET;
    if (inet_pton(AF_INET, ipAddress.c_str(), &(sin->sin_addr)) <= 0) {
        perror("inet_pton");
        close(sock);
        return macAddress;
    }

    if (ioctl(sock, SIOCGARP, &request) >= 0) {
        unsigned char* macPtr = (unsigned char*) request.arp_ha.sa_data;
        char macStr[18];
        snprintf(macStr, sizeof(macStr), "%02X:%02X:%02X:%02X:%02X:%02X",
                 macPtr[0], macPtr[1], macPtr[2],
                 macPtr[3], macPtr[4], macPtr[5]);
        macAddress = macStr;
    }
    close(sock);
#endif

    return macAddress;
}

int main() {
    std::string targetIP = "10.10.42.58"; // Replace with the IP address of the target host
    std::string macAddress = getMacAddress(targetIP);
    std::cout << "MAC Address of '" << targetIP << "': " << macAddress << std::endl;

    return 0;
}
