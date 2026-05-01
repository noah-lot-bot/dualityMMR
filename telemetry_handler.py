import paho.mqtt.client as mqtt
import json
import time
import asyncio
from data_handler import imu_reader

# raspberry pi IP on network
broker = "192.168.8.157"

# port supplied by Eclipse Mosquitto
port = 1883

# adjustable
topic = "duality/telemetry"

# create the client
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

# connect and start the client
client.connect(broker,port,60)
client.loop_start()

# non blocking data collection
async def telemetry_handler():
  try:
    while True:
      accelData, gyroData = imu_reader()
      imu_data = {
        "x_accel": accelData.xData,
        "y_accel": accelData.yData,
        "z_accel": accelData.zData,
        "x_rot": gyroData.xData,
        "y_rot": gyroData.yData,
        "z_rot": gyroData.zData
      }
      payload = json.dumps(imu_data)
      client.publish(topic, payload)
      await asyncio.sleep(0.1)
  finally:
    client.loop_stop()
    client.disconnect()
    
    



