import wiotp.sdk.device
import time
import random
myConfig = { 
    "identity": {
        "orgId": "pa0je7",
        "typeId": "testdevice",
        "deviceId":"27032002"
    },
    "auth": {
        "token": "y?MgR3saujsa3vV+g&"
    }
}
def myCommandCallback(cmd):
       print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
       m=cmd.data['command']
       if (m=="LIGHT ON"):
           print("light are on")
       elif(m=="LIGHT OFF"):
            print("lights off ")
       else:
           print("something wrong")

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()    
  
while True:
           Temperature = int(random.randint(-20,125))#temperature value by using random data 
           PH = int(random.randint(0,14))#ph 
           TSS = int(random.randint(0,3700))#turbidity data tss units is 'jts'
           Copper = int(random.randint(0,2000))#copper value present in water random data
           Ammonia  = int(random.randint(0,100))#ammonia and  nitrate value present in water  rgd
           nitrate=int(random.randint(0,100))
           Zinc = int(random.randint(0,100))#amount zinc present in water using random data
           Sulphate = int(random.randint(0,1000))#sulphate  present in water by using random data
           Sodium_chloride=int(random.randint(0,1000))#hardness present in water using random data
           myData={'PH':PH,'Temperature':Temperature,
             'Turbidity':TSS,'Copper':Copper,
             'Ammonia':Ammonia,'Nitrate':nitrate,          
              'Zinc':Zinc,
               'soidum_chloride':Sodium_chloride,'Sulphate':Sulphate}
           
           client.publishEvent(eventId="status",msgFormat="json", data=myData, qos=0, onPublish=None)
           print("Published data Successfully: %s", myData)
           client.commandCallback = myCommandCallback
           time.sleep(2)

client.disconnect()
