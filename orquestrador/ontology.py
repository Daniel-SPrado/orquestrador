from config import Ip
import requests
import time

class Ontology:
    def GetClient(gw, tag):
        payload = { 'mac': tag }
        result = requests.get(Ip.Gw(gw,'client'), params=payload).json()
        return result

    def GetService(gw, tag, mac, chipset):
        payload = { 'mac': mac, 'chipset': chipset }
        result = requests.get(Ip.Gw(gw, 'service'), params=payload).json()
        return result

    def GetData(gw, mac, chipset, number):
        payload = { 'chipset': chipset}
        result = requests.get(Ip.Gw(gw, 'data'), params=payload).json()
        return result

    def PostClient(gw, client):
        result =requests.post(Ip.Gw(gw, 'addClient'), data = client)
        return result

    def sendData(ip, param):
        payload = { param }
        url = 'http://' + str(ip) + str(param)
        print(url)
        print(ip)
        # if(ip == None):
        #     print('none')
        # else:
        #     result = requests.get(url)



class Check:
    def Client(client1, client2):
        if(client1 == client2):
            return True
        else:
            return False

    def Service(service1, service2):
        if(service1, service2):
            return True
        else:
            return False

    def Data(data1, data2):
        if(data1 == data2):
            return True
        else:
            return False 

