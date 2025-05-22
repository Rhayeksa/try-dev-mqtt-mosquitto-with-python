import sys

import paho.mqtt.client as paho
from text import txt
client = paho.Client()

if client.connect("localhost", 1883, 60) != 0:
    print("Couldn't connect to the mqtt broker")
    sys.exit(1)


# client.publish("test_topic", "Hi, paho mqtt client works fine x!", 0)
client.publish("test_topic", txt, 0)
client.disconnect()
