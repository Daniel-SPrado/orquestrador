from config import Ip
from ontology import Ontology, Check
from rule import Rule
from translate import dns
import time

time_sleep = 5
tag = '01:01:01:02'
mac = '01:01:01:02'
clients = {}

def main():
    regra = Rule.getRule('local', mac)
    if(regra):
        for item in regra:
            #Trocar 'cloud' -> 'local' para pegar os valores do sensor localmente
            valSensor = Rule.getSensor('cloud', item['value'][0]) #Pega o valor do sensor
            condSensor = item['value'][0]['condition'] #Pega a condição que o sensor deve ter
            
            valAtuador = Rule.getAtuador(item['value'][1]) #Pega
            param = item['value'][1]['param']

            Rule.execRule(valSensor, condSensor, valAtuador, param)
            print('---------------')
            
    else:
        print("nao existe regra")

while(True):
    main()
    print('##################')
    time.sleep(time_sleep)

