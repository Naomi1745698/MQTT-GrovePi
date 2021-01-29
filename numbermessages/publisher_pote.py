#grove publish that publishes a button true = pressed, false = not pressed
import paho.mqtt.client as mqtt 
from random import randrange, uniform
import time
import grovepi

# Connect the Potentiameter to A2
potentiometer = 2
#grovepi.pinMode(potentiometer,"INPUT")


mqttBroker ="test.mosquitto.org" 

client = mqtt.Client("Potentiameter")
client.connect(mqttBroker)

while True:
    x = grovepi.analogRead(potentiometer)
    print(x)
    
    client.publish("NumberMessage", x)
    print("Just published value to topic NumberMessage")
    time.sleep(1)
    
#stays always connected
