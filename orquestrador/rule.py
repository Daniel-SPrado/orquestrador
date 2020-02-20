from ontology import Ontology
from translate import dns
from scapy.all import ARP, Ether, srp
import ipaddress
import socket, struct, fcntl

clients = {}
#nome da interface que vai estar conectada na rede com os dispositivos
iface = "wlo1"

#ip e mascara da rede
target_ip = "172.16.9.1/24"

class Rule:
    def getRule(gw, tag):
        lista = []
        Client = Ontology.GetClient(gw, tag)
        if(Client):
            Service = Ontology.GetService(gw, tag, Client[0]['mac'], Client[0]['chipset'])
            if(Service):
                Data = Ontology.GetData(gw, Service[0]['mac'], Service[0]['chipset'], Service[0]['number'])
        return Data

    #Pegar valor do sensor
    def getSensor(gw, data):
        retorno = Ontology.GetData(gw, data['mac'], data['chipset'], data['number'])
        return retorno[0]['value'][0]

    #Tem que pegar o IP
    def getAtuador(data):
        #return Ontology.GetData('local', data['mac'], data['chipset'], data['number'])[0]['value'][0]
        return client_ip(data['mac'], )
        #return dns.translate(data['mac'], data['chipset'], data['number'])

    def execRule(sensor, cond, atuador, param):
        
        if(cond['param'] == '<'):
            if(sensor < cond['value']):
                print("Entrou na condição")
                Ontology.sendData(atuador, param)
            else:
                print("Nao fez a condição de <")
        elif(cond['param'] == '>'):
            if(sensor > cond['value']):
                print("Entrou na condição")
                Ontology.sendData(atuador, param)
            else:
                print("Nao fez a condição de >")
        elif(cond['param'] == '==' or cond['param'] == '='):
            if(sensor == cond['value']):
                print("Entrou na condição")
                Ontology.sendData(atuador, param)
            else:
                print("Nao fez a condição de ==")




def client_ip(mac):
    arp = ARP(pdst=target_ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp
    result = srp(packet, timeout=3, verbose=0)[0]

    
    for _, received in result:
        if received is not None:
            clients[received.hwsrc] = received.psrc
    
    return clients.get(mac)



# regra = Rule.getRule('01:01:01:01')
# print(Rule.getSensor('01:01:01:01', regra[0]))
# print(Rule.getAtuador('01:01:01:01', regra[2]))