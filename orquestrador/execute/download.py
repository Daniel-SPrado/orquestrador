from ontology import Ontology
import json
import requests

headers = {'content-type': 'application/json'}
url = 'https://uiot-dims.herokuapp.com'

payload = {'mac': '01:01:01:01'}
mac = '01:01:01:01'

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

    if(sensorC['chipset'] == sensorL['chipset'] and sensorL['mac'] == sensorC['mac'] and sensorL['number'] == sensorC['number']):
        if(conditionC['param'] == conditionL['param'] and conditionC['value'] == conditionL['value']):
            if(atuadorC['chipset'] == atuadorL['chipset'] and atuadorL['mac'] == atuadorC['mac'] and atuadorL['number'] == atuadorC['number']):
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
    print('----------------------------------')
    print(cloud)
    print('----------------------------------')
    print(local)
    print('##########################################')
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

desceRegra()













# def compareCient(cClient, lClient):
#     if(cClient[0]['mac'] == lClient[0]['mac'] and cClient[0]['chipset'] == lClient[0]['chipset']):
#         return True
#     else:
#         return False

# def compareService(x, y):
#     if(x['mac'] == y['mac'] and x['chipset'] == y['chipset'] and x['number'] == int(y['number'])):
#         return True
#     else:
#         return False

# def compareData(x, y):
#     if(x['mac'] == y['mac'] and x['chipset'] == y['chipset'] and x['number'] == int(y['number'])):
#         return True
#     else:
#         return False

# def getAll():
#     return Ontology.GetClient('cloud', mac), Ontology.GetClient('local', mac)

# def getRule(client):
#     return Ontology.GetService('cloud', tag, client[0]['mac'], client[0]['chipset']), Ontology.GetService('local', tag, client[0]['mac'], client[0]['chipset'])

# def addAll(client):
#     cliente = model.client(client[0])
#     Ontology.PostClient('local', cliente)
#     print('cadastrou client')
#     service = Ontology.GetService('cloud', tag, client[0]['mac'], client[0]['chipset'])
#     for item in service:
#         Ontology.PostService('local', item)
#         print('cadastrou service')
#         data = Ontology.GetData('cloud', item['mac'], item['chipset'], item['number'])
#         Ontology.PostData('local', data[0])
#     return True

# def addRule(service):
#     Ontology.PostService('local', service)
#     data = Ontology.GetData('cloud', service['mac'], service['chipset'], service['number'])
#     Ontology.PostData('local', data[0])

# def desceRegra():
#     cClient, lClient = getAll()
#     if(len(cClient) != 0 and len(lClient) == 0):
#         addAll(cClient)
#     elif(compareCient(cClient, lClient)):
#         cService, lService = getRule(cClient)
#         print(lService)
#         if(len(cService) != 0 and len(lService) == 0):
#             addRule(lService)
#         elif(len(cService) != 0 and len(lService) != 0):
#             for x in cService:
#                 isEqual = False
#                 for y in lService:
#                     if(compareService(x, y)):
#                         isEqual: True
#                         cData = Ontology.GetData('cloud', x['mac'], x['chipset'], x['number'])
#                         lData = Ontology.GetData('local', y['mac'], y['chipset'], y['number'])
#                         print(x)
#                         print(lData)
#                         if(len(cData) != 0 and len(lData) == 0):
#                             print('Local Data vazia, cadastrando...')
#                             # Ontology.PostData('local', cData[0])
#                         elif(len(cData) != 0 and len(lData) != 0):
#                             if(compareData(cData[0]['value'], lData[0]['value'])):
#                                 print('Datas iguais')
#                             else:
#                                 print('Datas são diferentes')
#                                 Ontology.PostData('local', cData)
#                 if(isEqual == False):
#                     addRule(x)
#         else:
#             print('nada acontece')
#     else:
#         print("Nada acontece")