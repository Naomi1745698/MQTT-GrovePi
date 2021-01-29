import paho.mqtt.client as mqtt
import time
import grovepi

#initialise button
buzzer = 8
grovepi.pinMode(buzzer,"OUTPUT")

#turn off buzzer initially
grovepi.digitalWrite(buzzer,0)

def on_message(client, userdata, message):
    print("received message: " ,str(message.payload.decode("utf-8")))
    if (str(message.payload.decode("utf-8")) == 'True'):
        #turn on buzzer
        grovepi.digitalWrite(buzzer,1)
    else:
        #turn off buzzer
        grovepi.digitalWrite(buzzer,0)

mqttBroker ="test.mosquitto.org"

client = mqtt.Client("Buzzer")
client.connect(mqttBroker) 

client.loop_start()

client.subscribe("OnOffMessage")
client.on_message=on_message 

time.sleep(30)
#disconnects after 30s