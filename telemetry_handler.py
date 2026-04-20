# static stability: RMS of pitch and roll
# jerk: derivative of acceleration
# vibration: fft of accel data
# zero moment point control
# pull voltage data? and cpu usage. should be easy enough
import paho.mqtt.client as mqtt
import json
import time
import asyncio
from data_handler import imu_reader

broker = "10.222.100.27"
port = 1883
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
    
    



