import json
import requests

url = 'https://uiot-dims.herokuapp.com/list/data?mac=78:2B:CB:BF:8F:61'
headers = {'content-type': 'application/json'}


if(1 == 1 and '3' == '2'):
    print(True)
else:
    print(False)

# # some JSON:
# x =  requests.get(url)

# y = json.loads(x.text)

# z = y[0]

# for i in z:
#     print(i, ': ', type(z[i]))

# url_send = 'https://uiot-dims.herokuapp.com/data'

# resp = requests.post(url_send, data=json.dumps(z), headers=headers)

# print(resp)
