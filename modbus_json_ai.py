import csv
from pyModbusTCP.client import ModbusClient
import sys
#----------------------------------------------------
# Abrir el archivo CSV y leer las direcciones IP
with open('ips.csv', 'r') as file:
    reader = csv.reader(file)
    ips = [row[0] for row in reader]
# Leer los dispositivos Modbus TCP
while True:
    for ip in ips:
        client = ModbusClient(host=ip, port=502, timeout=1)
        if client.open():
            result = client.read_holding_registers(0, 2)
            if result:
                print(f"Dispositivo {ip}, {result}")
            client.close()
        else:
            print(f"Dispositivo {ip}, NO encontrado")