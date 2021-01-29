#please note that with the sound sensor - if sounds are only played for half a
#second, there's a good chance that the sound sensor misses that sound. It is not
#broken and has been tested :)

import paho.mqtt.client as mqtt 
from random import randrange, uniform
import time
import grovepi

# Connect the sound sensor to A1
sound_sensor = 1
grovepi.pinMode(sound_sensor,"INPUT")

mqttBroker ="test.mosquitto.org" 

client = mqtt.Client("Sound Sensor")
client.connect(mqttBroker)

while True:
    sound = grovepi.analogRead(sound_sensor)
    print(sound)
    
    client.publish("NumberMessage", sound)
    print("Just published sound value to topic NumberMessage")
    time.sleep(1)
    
#stays always connected
