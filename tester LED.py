from firebase import firebase 
import serial
import serial.tools.list_ports as myPorts
import time

myDBConn =  firebase.FirebaseApplication("https://lc-login-84432-default-rtdb.asia-southeast1.firebasedatabase.app/", None)
myLEDStatus = myDBConn.get("ledstatus/status", None)

print(myLEDStatus)

for port in myPorts.comports():
    myPort = port[0]
    print(port[0])
    
mySerial = serial.Serial()
mySerial.baudrate = 115200
mySerial.port = myPort

mySerial.open()
while True:
    if myLEDStatus == 1:
        action = "1"
        action += ","
        mySerial.write(action.encode())
    else:
        action = "0"
        action +=","
        mySerial.write(action.encode())
        
    time.sleep(3)
    myLEDStatus = myDBConn.get("/ledstatus/status", None)
    print("LED Status is:", myLEDStatus)
