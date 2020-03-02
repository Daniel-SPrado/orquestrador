import requests
import time

main_url = 'https://uiot-dims.herokuapp.com'

client = '/client'
service = '/service'
data = '/data'

list_client = '/list/client'
list_service = '/list/service'
list_data = '/list/data'

headers = {'content-type': 'application/json'}

class Ontology:
    def GetClient(mac):
        payload = { 'mac': mac }
        result = requests.get(Ip.Gw(gw,'client'), params=payload).json()
        return result