# static stability: RMS of pitch and roll
# jerk: derivative of acceleration
# vibration: fft of accel data
# zero moment point control
# pull voltage data? and cpu usage. should be easy enough
import paho.mqtt.client as mqtt
import json
import time

broker = "10.137.166.27"
port = 1883
topic = "duality/telemetry/imu"

# create the client
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

# subscribe the client to messages in case of disconnect
def on_connect(client, userdata, flags, reason_code, properties):
  client.subscribe("$SYS/#)
                   
# connect and start the client
client.connect(broker,port,60)
client.on_connect = on_connect
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
    
    



