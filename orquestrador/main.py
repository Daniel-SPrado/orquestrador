from scapy.all import ARP, Ether, srp
import ipaddress
import socket, struct, fcntl

clients = {}

def client_ip(mac, iface, network_address):
    arp = ARP(pdst=target_ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp
    result = srp(packet, timeout=3, verbose=0)[0]

    
    for _, received in result:
        if received is not None:
            clients[received.hwsrc] = received.psrc
    
    return clients.get(mac)

#nome da interface que vai estar conectada na rede com os dispositivos
iface = "wlo1"

#ip e mascara da rede
target_ip = "172.16.9.1/24"

print(client_ip('b8:27:eb:1b:3e:36',iface, target_ip))
print(clients)