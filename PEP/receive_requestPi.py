import paho.mqtt.client as mqtt
import csv

MQTT_SERVER = "localhost"
MQTT_PATH = "requests" # topic

# subscribe to the topic requests
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(MQTT_PATH)

# print & save the received msg
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    with open(r'received.csv', 'a') as f:
        f.write(msg.payload)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# connect to the broker
client.connect(MQTT_SERVER, 1883, 60)

client.loop_forever()
