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
        Client = Ontology.GetClient(gw, tag)
        Lista = []
        if(Client):
            Service = Ontology.GetService(gw, tag, Client[0]['mac'], Client[0]['chipset'])
            for item in Service:
                Data = Ontology.GetData(gw, item['mac'], item['chipset'], item['number'])
                if(len(Data) != 0):
                    Lista.append(Data[0])
                Data = None
        return Lista

    #Pegar valor do sensor
    def getSensor(gw, data):
        retorno = Ontology.GetData(gw, data['mac'], data['chipset'], data['number'])
        if retorno != []:
            return retorno[0]['value']
        return {}

    #Tem que pegar o IP
    def getAtuador(data):
        retorno_ip = client_ip(data['mac'], )
        print("O IP é: " + str(retorno_ip))
        if( retorno_ip is None ):
            return dns.translate(data['mac'])
        else:
            return client_ip(data['mac'], )

    def execRule(sensor, cond, atuador, param):
        print("O valor do sensor é: " + sensor)
        print("A condição é ser: " + cond['param'] + " a/que " + cond['value'])
        if(cond['param'] == '<'):
            if(sensor < cond['value']):
                print("Entrou na condição de <")
                Ontology.sendData(atuador, param)
            else:
                print("Nao fez a condição de <")
        elif(cond['param'] == '>'):
            if(sensor > cond['value']):
                print("Entrou na condição de >")
                Ontology.sendData(atuador, param)
            else:
                print("Nao fez a condição de >")
        elif(cond['param'] == '==' or cond['param'] == '='):
            if(sensor == cond['value']):
                print("Entrou na condição de ==")
                Ontology.sendData(atuador, param)
            else:
                print("Nao fez a condição de ==")

    def execRule2(atuador, param):
       Ontology.sendData(atuador, param)

    def ParseRule(value, cond, operator):
        if(operator == '<'):
            return value < cond
        elif(operator == '>'):
            return value > cond
        elif(operator == '==' or operator == '='):
            return value == cond    
        return False

    def ParseBoolean(value1, value2, operator):
        if(operator == 'and'):
            return value1 and value2
        elif(operator == 'or'):
            return value1 or value2

        return False    


def client_ip(mac):
    arp = ARP(pdst=target_ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp
    result = srp(packet, timeout=3, verbose=0)[0]

    
    for _, received in result:
        if received is not None:
            clients[received.hwsrc] = received.psrc
    
    return clients.get(mac)

print(client_ip('B8:27:EB:D3:5A:CD'))