from config import Ip
from ontology import Ontology, Check
from rule import Rule
from translate import dns
import time

tag = '01:01:01:02'
mac = '01:01:01:02'

clients = {}

def main():
    regra = Rule.getRule('local', mac)
    if(regra):
        for item in regra:
            data_value = item['value']
            s1 = data_value['sensor1']
            actuator = data_value['actuator']

            if s1 is None or actuator is None:
                raise Exception('You have no data here.')

            val_s1 = Rule.getSensor('local', s1)

            if 'sensor1' in val_s1:
                s1_cond = Rule.ParseRule(val_s1['sensor1']['value'], s1['value'], s1['param'])

            operator = 'or'
            bind_operator = data_value['operator']

            if bind_operator is not None:
                operator = bind_operator

            s2_cond = False
            s2 = data_value['sensor2']
            if s2 is not None:
                val_s2 = Rule.getSensor('local', s2)
                if 'sensor2' in val_s2:
                    s2_cond = Rule.ParseRule(val_s2['sensor2']['value'], s2['value'], s2['param'])


            val_atuador = Rule.getAtuador(actuator)
            param_atuador = actuator['param']

            if Rule.ParseBoolean(s1_cond, s2_cond, operator):
                Rule.execRule2(val_atuador, param_atuador)

            print('---------------')
            
    else:
        print("não existe regra")

while(True):
    main()
    print('##################')
    time.sleep(time_sleep)

