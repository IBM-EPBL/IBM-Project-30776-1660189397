#IBM Watson IOT platform
#pip install wiotp-sdk
import wiotp.sdk.device
import time
import random
myConfig = {
    "identity": {
        "orgID":"pa0je7",
        "typeID":"testdevice",
        "deviceID":"27032002"
        },
    "auth": {
        "token": "y?MgR3saujSA3vV+g&"
        }
    }
def mycommandcallback(cmd):
    print("Message received from IBM Watson IOT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']
    if(m=="Sensor ON"):
        print("*****///SENSORS ARE ON/////*****")
    elif(m=="Sensors OFF"):
        print("*****///SENSORS ARE OFF/////*****")
    else:
        print("*****//WRONG COMMAND/////*****")

client=wiotp.sdk.device.Deviceclient(config=myConfig, logHandlers=None)
client.connect()

while true:
    temp=random.randint(10,50)
    humid=random.randint(0,100)
    PH=random.randint(1,14)
    turbid=random.randint(10,250)
    myData={'temperature':temp, 'humidity':humid, 'PH':PH, 'turbidity':turbid}
    client.publishEvent(eventID="status", msgFormat="json", data=myData, qos=0, onpublish=None)
    print("Published data successfully: %s",myData)
    client.commandcallback = mycommandcallback
    time.sleep(2)
client.disconnect()    
