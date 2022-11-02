from os import device_encoding
import wiotp.sdk.device
import time
import random
myconfig = {
    "identity": {
    "orgID": "pa0je7"
    "typeID":test device
    "deviceID":27032002
    }
    "auth": {
        "token" "bDlt!*p*D8IF8VvQJS"
            }
    
}
def mycommandcallback(cmd):
    print("message received from IBM IoT platform : %s" % cmd.data ['command'])
    m=cmd.data['command']

    client = wiotp.sdk.Deviceclient(config=myconfig, logHandlers=none)
    client.connect()

    while true:
        temp=random.randint(-20,125)
        hum=random.randint(0,100)
        myDat{'temperature':temp, 'humidity':hum}
        client.publishEvent(EventID="status", msg format="json", data=mydata, qos=0)
        print("published data successfully: %s", mydata)
        Client.commandcallback=mycommandcallback
        time.sleep(2)
        client.disconnect()