#grove publish that publishes a button true = pressed, false = not pressed
import paho.mqtt.client as mqtt 
from random import randrange, uniform
import time
from grovepi import *

#ultrasonic ranger should be in port D5
ultrasonic_ranger = 5

mqttBroker ="test.mosquitto.org" 

client = mqtt.Client("Ultrasonic")
client.connect(mqttBroker)

while True:
    try:
        #read distance value from ulttrasonic
        distant = ultrasonicRead(ultrasonic_ranger)
        print(distant,'cm')

        client.publish("NumberMessage", distant)
        print("Just published distance to topic NumberMessage")
        time.sleep(1)
        
    except TypeError:
        print("Error")
    
#stays always connected