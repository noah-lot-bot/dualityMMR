# static stability: RMS of pitch and roll
# jerk: derivative of acceleration
# vibration: fft of accel data
# zero moment point control
# pull voltage data? and cpu usage. should be easy enough
from paho-mqtt import client as mqtt
import json
import time

broker = "localhost"
port = 1883
topic = duality/telemetry/imu

client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.Version2)

client.connect(broker,port,60)

client.loop_start()

try:
  while True:
    



