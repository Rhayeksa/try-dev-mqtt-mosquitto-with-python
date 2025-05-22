import paho.mqtt.publish as publish

from text import txt

publish.single(
    topic="test/topic",
    # payload="Halo dari Python!",
    payload=txt,
    hostname="localhost",
    port=1883
)
print("Message sent.")
