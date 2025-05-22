import warnings

import paho.mqtt.client as mqtt

warnings.filterwarnings("ignore", category=DeprecationWarning)

# Callback saat berhasil terhubung


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("test/topic")

# Callback saat menerima pesan


def on_message(client, userdata, msg):
    print(f"Message received on topic {msg.topic}: {msg.payload.decode()}")


client = mqtt.Client(
    # callback_api_version=5,
    client_id="x",
    protocol=mqtt.MQTTv311
)
# client = mqtt.Client(callback_api_version=5)

client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)
client.loop_forever()
