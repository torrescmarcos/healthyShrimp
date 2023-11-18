import minimalmodbus
import serial
import time
import json
import requests
import sys
#///////////////////////////////////////////////////
c = minimalmodbus.Instrument('COM3',1,debug=False)
c.serial.baudrate=19200
c.serial.bytesize =8
c.serial.parity = serial.PARITY_NONE
c.serial.stopbits = 1
c.serial.timeout = 0.1
c.address = 1
c.mode = minimalmodbus.MODE_RTU
c.clear_buffers_before_each_transaction = True
#//////////////////////////////////////////////////
r = [0.0, 0.0, 0.0]
while True:
    try:
        r = [round(c.read_float(1,3,2,0),1), round(c.read_float(3,3,2,0),1), round(c.read_float(5,3,2,0),1)]
    except:
        print(sys.exc_info()[0])

    jd = json.dumps({'O2':r[0],'pH':r[1],'Temp.':r[2]})
    print(jd)
    try:
        response = requests.post('https://demo.thingsboard.io/api/v1/1kS5RUH5sr8VQH85rfLm/telemetry', data=jd)
        if(response.status_code != 200):
            print(response)
    except:
        print(sys.exc_info()[0])
    time.sleep(10)
