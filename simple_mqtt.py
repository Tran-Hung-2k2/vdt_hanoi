# pip install adafruit-io
import random
import time
import sys
from Adafruit_IO import MQTTClient

AIO_USERNAME = "your_name"
AIO_KEY = "your_key"

client = MQTTClient(AIO_USERNAME, AIO_KEY)

client.connect()
client.loop_background()
time.sleep(5)

while True:
    value = random.randint(0, 100)
    client.publish("your_feed", value)
    time.sleep(30)
