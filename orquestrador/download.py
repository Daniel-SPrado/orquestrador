from ontology import Ontology
import json
import requests
import time

time_sleep = 10
headers = {'content-type': 'application/json'}
url = 'https://uiot-dims.herokuapp.com'

# payload = {'mac': '01:01:01:01'}
mac = '01:01:01:02'

def compareClient(cloud, local):
    cloud = cloud[0]
    local = local[0]
    if(cloud['mac'] == local['mac'] and local['chipset'] == cloud['chipset']):
        return True
    else:
        return False

def compareService(cloud, local):
    if(cloud['mac'] == local['mac'] and local['chipset'] == cloud['chipset'] and local['number'] == cloud['number']):
        compareAndPostData(cloud, local)
        return True
    else:
        return False

def compareValue(cloud, local):
    sensorC = cloud[0]
    sensorL = local[0]
    conditionC = cloud[0]['condition']
    conditionL = local[0]['condition']
    atuadorC = cloud[1]
    atuadorL = local[1]
    # print(sensorC, sensorL)
    # print('++++++++++')
    # print(conditionC, conditionL)
    # print('++++++++++')
    # print(atuadorC, atuadorL)
    if(sensorC['chipset'] == sensorL['chipset'] and sensorL['mac'] == sensorC['mac'] and sensorL['number'] == sensorC['number']):
        if(conditionC['param'] == conditionL['param'] and conditionC['value'] == conditionL['value']):
            if(atuadorC['chipset'] == atuadorL['chipset'] and atuadorL['mac'] == atuadorC['mac'] and atuadorL['number'] == atuadorC['number'] and atuadorC['param'] == atuadorL['param']):    
                return True
            else:
                return False
        else:
            return False
    else:
        return False
    

def compareData(cloud, local):
    cloudValue = cloud['value']
    localValue = local['value']
    if(compareValue(cloudValue, localValue)):
        return True
    else:
        return False

def compareAndPostData(cloud, local):
    cloud = Ontology.GetData('cloud', cloud['mac'], cloud['chipset'], cloud['number'])
    local = Ontology.GetData('local', local['mac'], local['chipset'], local['number'])
    if(len(cloud) == 0 and len(local) == 0 or len(cloud) == 0 and len(local) != 0):
        print('nao faça nada com data')
    elif(len(cloud) != 0 and len(local) == 0):
        print('Postando data')
        result = requests.post("http://localhost:5000/data", data=json.dumps(cloud[0]), headers=headers)
    elif(len(cloud) != 0 and len(local) != 0):
        if(compareData(cloud[0], local[0])):
            print('datas são iguais')
        else:
            print('datas são diferentes, postando...')
            result = requests.post("http://localhost:5000/data", data=json.dumps(cloud[0]), headers=headers)


def desceRegra():
    cloudClient = Ontology.GetClient('cloud', mac)
    localClient = Ontology.GetClient('local', mac)
    
    if(len(cloudClient) == 0):
        print('Não faça nada')
    elif(len(localClient) == 0):
        result = requests.post("http://localhost:5000/client", data=json.dumps(cloudClient[0]), headers=headers)
        print(result)
    elif(compareClient(cloudClient, localClient)):
        cloudService = Ontology.GetService('cloud', mac, mac, mac)
        localService = Ontology.GetService('local', mac, mac, mac)
        
        if(len(cloudService) == 0):
            print('Não faça nada 2')
        elif(len(localService) == 0):
            for item in cloudService:
                result = requests.post("http://localhost:5000/service", data=json.dumps(item), headers=headers)
                print(result)
        else:
            for x in cloudService:
                aux = False
                for y in localService:
                    if(compareService(x, y)):
                        print('serviços iguais')
                        aux = True
                
                if(aux == False):
                    print('postando data')
                    result = requests.post("http://localhost:5000/service", data=json.dumps(x), headers=headers)
    else:
        print('not okay')

while(True):
    desceRegra()
    print('----------------------------------------------')
    time.sleep(time_sleep)