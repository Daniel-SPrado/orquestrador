import json
import requests

url = 'https://uiot-dims.herokuapp.com/list/data?mac=78:2B:CB:BF:8F:61'
headers = {'content-type': 'application/json'}


# # some JSON:
x =  requests.get(url, headers=headers).json()

print(type(x[0]))

y = x[0]
x = x[0]

# y = json.loads(x.text)

# z = y[0]

# for i in z:
#     print(i, ': ', type(z[i]))

# url_send = 'https://uiot-dims.herokuapp.com/data'

# resp = requests.post(url_send, data=json.dumps(z), headers=headers)

# print(resp)
