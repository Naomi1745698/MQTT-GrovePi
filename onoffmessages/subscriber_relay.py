import paho.mqtt.client as mqtt
import time
import grovepi

#initialise button
relay = 3
grovepi.pinMode(relay,"OUTPUT")

#turn off relay initially
grovepi.digitalWrite(relay,0)

def on_message(client, userdata, message):
    print("received message: " ,str(message.payload.decode("utf-8")))
    if (str(message.payload.decode("utf-8")) == 'True'):
        #turn on relay
        grovepi.digitalWrite(relay,1)
    else:
        #turn off relay
        grovepi.digitalWrite(relay,0)

mqttBroker ="test.mosquitto.org"

client = mqtt.Client("Relay")
client.connect(mqttBroker) 

client.loop_start()

client.subscribe("OnOffMessage")
client.on_message=on_message 

time.sleep(30)
#disconnects after 30s