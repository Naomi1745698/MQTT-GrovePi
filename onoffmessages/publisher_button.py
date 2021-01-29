#grove publish that publishes a button true = pressed, false = not pressed
import paho.mqtt.client as mqtt 
from random import randrange, uniform
import time
import grovepi

#initialise button
button = 6
grovepi.pinMode(button,"INPUT")

mqttBroker ="test.mosquitto.org" 

client = mqtt.Client("Button")
client.connect(mqttBroker)

while True:
    if(grovepi.digitalRead(button)):
        client.publish("OnOffMessage", True)
        print("Just published 'True' to topic OnOffMessage")
        time.sleep(1)
    else:
        client.publish("OnOffMessage", False)
        print("Just published 'False' to topic OnOffMessage")
        time.sleep(1)
    
#stays always connected