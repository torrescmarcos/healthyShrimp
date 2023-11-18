from pyModbusTCP.client import ModbusClient
import numpy
import time
import csv
import sys
#-------------------------------------------------
# Abrir el archivo CSV y leer las direcciones IP
with open('ips.csv', 'r') as file:
    reader = csv.reader(file)
    ips = [row[0] for row in reader]
while True:
    try:
        for ip in ips:
            i = "'"+ip+"'"
            c = ModbusClient(host=i, port=502, unit_id=1, auto_open=True)
            r = c.read_holding_registers(0,6)
            tmp=numpy.array(r,numpy.int16)
            tmp.dtype = numpy.float32
            print(i)
            c.close()
            print(ips)
    except:
        print(sys.exc_info()[0])
    time.sleep(3)