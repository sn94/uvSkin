import serial, time,threading
 
"""arduino = serial.Serial('COM10', 9600) 
arduino.setDTR(False)
time.sleep(1)
arduino.flushInput()
arduino.setDTR(True)
"""

def notificar(  iuv  ): 
    url="http://192.168.0.12:8080/uvapp/notificar/"+ str( iuv ) 
    import requests
    req = requests.get( url   )
    print( req.status_code, req)

notificar( 5)

"""while True:
    try:
        line = arduino.readline()
        print(line, "\n")
        time.sleep(200)
    except:
        print("hubo un error")
        break

arduino.close()"""


