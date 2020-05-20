'''
send request to Raspberry via MQTT
'''
import paho.mqtt.publish as publish

MQTT_SERVER = "192.168.1.63"
MQTT_PATH = "requests"

def get_axx(fields):
    publish.single(MQTT_PATH, str(fields), hostname=MQTT_SERVER)
