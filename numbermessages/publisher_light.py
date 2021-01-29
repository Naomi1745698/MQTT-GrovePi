import paho.mqtt.client as mqtt 
from random import randrange, uniform
import time
import grovepi

# Connect the light sensor to A0
light_sensor = 0

mqttBroker ="test.mosquitto.org" 

client = mqtt.Client("Light Sensor")
client.connect(mqttBroker)

while True:
    light = grovepi.analogRead(light_sensor)
    
    client.publish("NumberMessage", light)
    print("Just published light value to topic NumberMessage")
    time.sleep(1)
    
#stays always connected
