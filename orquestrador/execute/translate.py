
class dns:
    def translate(mac):
        data = [
                #Luzes
                {
                    'mac': '24:6F:28:16:CC:88',
                    'ip': "172.16.9.178"
                },
                #MAC E IP DOS COMANDOS DO AR CONDICIONADO
                {
                    'mac': '30:AE:A4:F4:D7:94',
                    'ip': "172.16.9.161"
                }
            ]
        for i in data:
            if(mac == i['mac']):
                return i['ip']
        
