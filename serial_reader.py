
import serial, time,threading
 
arduino = serial.Serial('COM14', 9600) 
arduino.setDTR(False)
time.sleep(1)
arduino.flushInput()
arduino.setDTR(True)

alerted_state= False
iuv_alerted_state= 1

def notificar(  iuv  ): 
    url="http://192.168.0.12:8080/uvapp/notificar/"+ str( iuv ) 
    import requests
    req = requests.get( url   )
    print( req.status_code, req)

#notificar( 5)

while True:
    try:
        line = arduino.readline().decode("utf-8")  
        iuv= int(  line )
        if iuv > 2  and  iuv_alerted_state != iuv :
            iuv_alerted_state= iuv 
            notificar( iuv )
        else:
            print("IUV muy bajo aun")
    except:
        print("hubo un error")
        break

arduino.close()

