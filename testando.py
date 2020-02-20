# def desceRegra():
#     cClient = Ontology.GetClient('cloud', mac)
#     lClient = Ontology.GetClient('local', mac)
#     if(len(cClient) != 0 and len(lClient) == 0):
#         Ontology.PostClient('local', cClient[0])
#     elif(cClient[0]['mac'] == lClient[0]['mac'] and cClient[0]['chipset'] == lClient[0]['chipset']):
#         cService = Ontology.GetService('cloud', tag, cClient[0]['mac'], cClient[0]['chipset'])
#         lService = Ontology.GetService('local', tag, cClient[0]['mac'], cClient[0]['chipset'])
#         if(len(cService) == 0 and len(lService) == 0):
#             for x in cService:
#                 auxiliar = 0
#                 for y in lService:
#                     if(x['mac'] == y['mac'] and x['chipset'] == y['chipset'] and x['number'] == y['number']):
#                         cData = Ontology.GetData('cloud', x['mac'], x['chipset'], x['number'])
#                         lData = Ontology.GetData('local', y['mac'], y['chipset'], y['number'])
#                         if(cData[0] == lData[0]):
#                             print('não faz nada com data')
#                         else:
#                             print('Cadastra cData[0] localmente')
#                         auxiliar = auxiliar + 1
#                 if(auxiliar == 0):
#                     print("Cadastrar service x localmente")
#                     print("Cadastrar data DE x localmente") 
#             print('Service e data não existem')
#     else:
#         print("Nada acontece")

for s in i['sensor']:
                    valSensor = Rule.getSensor(s['dest'])