from config import Ip
from ontology import Ontology, Check
from rule import Rule
from translate import dns
import requests
import time

tag = '01:01:01:01'
mac = '01:01:01:01'
clients = {}

def main():
    regra = Rule.getRule('local', mac)
    print(regra)
    if(regra):
        for item in regra:
            valSensor = Rule.getSensor('local', item['value'][0])
            condSensor = item['value'][0]['condition'] #Pega a condição do sensor
            
            valAtuador = Rule.getAtuador(item['value'][1])  
            param = item['value'][1]['param']

            Rule.execRule(valSensor, condSensor, valAtuador, param)
            print('---------------')
            
    else:
        print("não existe regra")

main()
