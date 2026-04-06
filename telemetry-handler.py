# static stability: RMS of pitch and roll
# jerk: derivative of acceleration
# vibration: fft of accel data
# zero moment point control
# pull voltage data? and cpu usage. should be easy enough
import paho.mqtt.client as mqtt
import json
import time
from data_handler import imu_reader

broker = "localhost"
port = 1883
topic = "duality/telemetry"

# create the client
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

# subscribe the client to messages in case of disconnect
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

# connect and start the client
client.connect(broker,port,60)
client.on_message = on_message
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
    
    



