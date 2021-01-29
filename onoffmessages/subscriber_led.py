import paho.mqtt.client as mqtt
import time
import grovepi

#initialise button
led = 3
grovepi.pinMode(led,"OUTPUT")

#turn off light initially
grovepi.digitalWrite(led,0)

def on_message(client, userdata, message):
    print("received message: " ,str(message.payload.decode("utf-8")))
    if (str(message.payload.decode("utf-8")) == 'True'):
        #turn on light
        grovepi.digitalWrite(led,1)     #turns on light 1
    else:
        #turn off light
        grovepi.digitalWrite(led,0)     #turns off light 1

mqttBroker ="test.mosquitto.org"

client = mqtt.Client("LED")
client.connect(mqttBroker) 

client.loop_start()

client.subscribe("OnOffMessage")
client.on_message=on_message 

time.sleep(30)
#disconnects after 30s