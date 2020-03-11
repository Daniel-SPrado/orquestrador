from config import Ip
import translate
import requests
import time

headers = {'content-type': 'application/json'}

class Ontology:
    #Return client, service and data
    def GetClient(gw, tag):
        payload = { 'mac': tag }
        result = requests.get(Ip.Gw(gw,'client'), params=payload).json()
        return result

    def GetService(gw, tag, mac, chipset):
        payload = { 'mac': mac, 'chipset': chipset }
        result = requests.get(Ip.Gw(gw, 'service'), params=payload).json()
        return result

    def GetData(gw, mac, chipset, number):
        payload = { 'mac': mac, 'chipset': chipset, 'serviceNumber': number }
        result = requests.get(Ip.Gw(gw, 'data'), params=payload).json()
        return result

    #Create client, service and data
    def PostClient(gw, client):
        result = requests.post(Ip.Gw(gw, 'addClient'), data = client, headers=headers)
        return result

    def PostService(gw, service):
        result = requests.post(Ip.Gw(gw, 'addService'), data = service, headers=headers)
        return result

    def PostData(gw, data):
        result = requests.post(Ip.Gw(gw, 'addData'), data = data, headers=headers)
        return result

    #Send info
    def sendData(ip, param):
        payload = { param }
        if ip is None:
           ip = translate.dns.translate() 
        url = 'http://' + ip + str(param)
        print(url)
        print(param)
        result = requests.get(url)
        print(result)




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

