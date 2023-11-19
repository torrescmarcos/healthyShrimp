import csv
from pyModbusTCP.client import ModbusClient
import sys
import json
import requests
#----------------------------------------------------
# Abrir el archivo CSV y leer las direcciones IP
with open('ips.csv', 'r') as file:
    reader = csv.reader(file)
    ips = [row[0] for row in reader]
# Leer los dispositivos Modbus TCP
url = "https://jsononline.net/es/json-checker"
while True:
    for ip in ips:
        client = ModbusClient(host=ip, port=502, timeout=1)
        if client.open():
            result = client.read_holding_registers(0, 1)
            if result:
                print(f"Dispositivo {ip}, {result}")
                data = {}
                data['Peso'] = str(result[0])
                jsonData = json.dumps(data)
                print(jsonData)
                # response = requests.post(url, json=jsonData)
                # print(response.text)
            client.close()
        else:
            print(f"Dispositivo {ip}, NO encontrado")