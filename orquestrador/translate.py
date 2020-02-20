
class dns:
    def translate(mac, chipset, number):
        data = [
                #Luz02
                {
                    'mac': '54321',
                    'chipset': '54321',
                    'number': 1,
                    'ip': "172.16.9.178"
                },
                #Controla ar software
                {
                    'mac': '9A:49:4F:54:33:E1',
                    'chipset': '0C:3F:9F:89:5E:9F',
                    'number': 1,
                    'ip': '172.16.9.161'
                },
                #Controla AC SPEED
                {
                    'mac': '12',
                    'chipset': '12',
                    'number': 1,
                    'ip': "172.16.9.161"
                }
            ]
        for i in data:
            if(mac == i['mac'] and chipset == i['chipset'] and number == i['number']):
                return i['ip']
        
