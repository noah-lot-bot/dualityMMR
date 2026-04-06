# static stability: RMS of pitch and roll
# jerk: derivative of acceleration
# vibration: fft of accel data
# zero moment point control
# pull voltage data? and cpu usage. should be easy enough
from paho.mqtt import client as mqtt
import json
import time

broker = "10.137.166.27"
port = 1883
topic = "duality/telemetry/imu"

# create the client
client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)

# connect the client to the broker (Docker container)
client.connect(broker,port,60)

# start the messaging client
client.loop_start()
  
try:
  while True:
    reading = imu_reader()
    if reading[0] is not None:
      accelData, gyroData = reading
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
      time.sleep(0.1)
except KeyboardInterrupt:
  client.loop_stop()
  client.disconnect()
    
    



