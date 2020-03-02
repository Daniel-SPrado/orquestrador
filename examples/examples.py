REGRA
CLIENT
{
  "clientTime": 1000000000.1111,
  "tags": [
      "01:01:01:01"
  ],
  "name": "UIoT devices",
  "chipset": "01:01:01:01",
  "mac": "01:01:01:01",
  "serial": "01:01:01:01",
  "processor": "none",
  "channel": "Wi-fi",
  "location": "-15.7757876:-48.077829"
}
SERVICE
{
    "chipset": "01:01:01:01",
    "clientTime": 1000000000.1,
    "mac": "01:01:01:01",
    "name": "PL-01",
    "number": 1,
    "numeric": 1,
    "parameter": "",
    "tags": [
        "01:01:01:01"
    ],
    "unit": ""
}
DATA
{
    "chipset": "01:01:01:01",
    "clientTime": 1000000000.1,
    "mac": "01:01:01:01",
    "sensitive": 1,
    "serviceNumber": 1,
    "tags": [
        "01:01:01:01"
    ],
    "value": [
        {
          "chipset": "Linux",
          "mac": "78:2B:CB:BF:8F:61",
          "number": 777365,
          "condition": { 
            "param": "==", 
            "value": "0" 
          }
        },
        {
          "chipset": "54321",
          "mac": "30:ae:a4:f4:dd:24",
          "number": 1,
          "param": "/LIGHT1=OFF"
        }
    ]
}



SWAGGER EDITOR
CLIENT
{
  "clientTime": 1000000000.1111,
  "tags": [
    "example-tag"
  ],
  "name": "Raspberry PI",
  "chipset": "AMD 790FX",
  "mac": "FF:FF:FF:FF:FF:FF",
  "serial": "C210",
  "processor": "Intel I3",
  "channel": "Ethernet",
  "location": "-15.7757876:-48.077829"
}
SERVICE
{
  "clientTime": 1000000000.1,
  "tags": [
    "example-tag"
  ],
  "number": 3,
  "chipset": "AMD 790FX",
  "mac": "FF:FF:FF:FF:FF:FF",
  "name": "Get temp",
  "parameter": "temperature",
  "unit": "°C",cd
  "numeric": 1
}
DATA
{
  "clientTime": 1000000000.1,
  "tags": [
    "example-tag"
  ],
  "sensitive": 1,
  "chipset": "AMD 790FX",
  "mac": "FF:FF:FF:FF:FF:FF",
  "serviceNumber": 3,
  "value": [
    "20.2",
    "30.0"
  ]
}

CAMERA
CLIENT
  {
    "channel": "HTTP",
    "chipset": "Windows",
    "location": "-15.7797:-47.9297",
    "mac": "D0:94:66:B4:79:6E",
    "name": "Windows",
    "processor": "Intel64 Family 6 Model 142 Stepping 12, GenuineIntel",
    "serial": "0000000000000000",
    "time": "2020-02-14 18:29:48.894185"
  },
SERVICE
{
    "channel": "HTTP",
    "chipset": "Windows",
    "mac": "D0:94:66:B4:79:6E",
    "name": "MIA",
    "number": "777365",
    "numeric": "",
    "parameter": "",
    "time": "2020-02-14 18:29:49.443652",
    "unit": ""
},
DATA
{
    "channel": "HTTP",
    "chipset": "Windows",
    "mac": "D0:94:66:B4:79:6E",
    "sensitive": 0,
    "serviceNumber": "777365",
    "time": "2020-02-14 18:29:49.443652",
    "value": "2"
},


SENSOR TEMPERATURA
'mac': '321',
'chipset': '321',
'number': 1,



LAMPADA
'mac': '54321',
'chipset': '54321',
'number': 1,
'ip': "172.16.9.178"

# AC-temp
# 'mac': '12345',
# 'chipset': '12345',
# 'number': 1,
# 'ip': "172.16.9.178"

AC-speed
'mac': '12',
'chipset': '12',
'number': 1,
'ip': "172.16.9.178"