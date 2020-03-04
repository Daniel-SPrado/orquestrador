class Ip:
    def Gw(gw, option):
        if(option == 'client'):
            seletor = '/list/client'
        if(option == 'service'):
            seletor = '/list/service'
        if(option == 'data'):
            seletor = '/list/data'
        if(option == 'addClient'):
            seletor = '/client'
        if(option == 'addService'):
            seletor = '/service'
        if(option == 'addData'):
            seletor = '/data'
        if(gw == 'cloud'):
            gateway = 'https://uiot-dims.herokuapp.com'
        if(gw == 'local'):
            gateway = 'http://localhost:5000'
        return gateway + seletor
        #https://uiot-dims.herokuapp.com

    def Mac():
        return '02:02:02:02'

