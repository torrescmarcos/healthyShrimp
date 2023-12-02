from pymodbus.client.sync import ModbusTcpClient
from concurrent.futures import ThreadPoolExecutor
import csv
#----------------------------------------------------
# Abrir el archivo CSV y leer las direcciones IP
with open('ips.csv', 'r') as file:
    reader = csv.reader(file)
    ips = [row[0] for row in reader]

# Función para leer los registros de un PLC
def read_plc(plc_ip):
    # Conexión al PLC
    client = ModbusTcpClient(plc_ip, timeout=1)
    # Lectura de los registros
   
    result = client.read_holding_registers(0, 1)
    
    # Impresión de los registros
    print(f"{plc_ip}: {result.registers}")

    # Cierre de la conexión
    client.close()

# Creación de un ThreadPoolExecutor con 3 hilos
while True:
    with ThreadPoolExecutor(max_workers=3) as executor:
        # Llamada a la función read_plc para cada dirección IP
        for plc_ip in ips:
            executor.submit(read_plc, plc_ip)
