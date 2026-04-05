# static stability: RMS of pitch and roll
# jerk: derivative of acceleration
# vibration: fft of accel data
# zero moment point control
# pull voltage data? and cpu usage. should be easy enough
from paho.mqtt import client as mqtt
import json
import time
import qwiic_ism330dhcx

broker = "10.137.166.27"
port = 1883
topic = "duality/telemetry/imu"

# create the client
client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)

# connect the client to the broker (Docker container)
client.connect(broker,port,60)

# start the messaging client
client.loop_start()

# read the imu data
def = imu_reader():
  myIsm = qwiic_ism330dhcx.QwiicISM330DHCX()
  myIsm.begin()
  while myIsm.get_device_reset() == False:
    time.sleep(1)

    myIsm.set_device_config()
    myIsm.set_block_data_update()
 
    myIsm.set_accel_data_rate(myIsm.kXlOdr104Hz)
    myIsm.set_accel_full_scale(myIsm.kXlFs4g)
 
    myIsm.set_gyro_data_rate(myIsm.kGyroOdr104Hz)
    myIsm.set_gyro_full_scale(myIsm.kGyroFs500dps)
 
    myIsm.set_accel_filter_lp2()
    myIsm.set_accel_slope_filter(myIsm.kLpOdrDiv100)
 
    myIsm.set_gyro_filter_lp1()
    myIsm.set_gyro_lp1_bandwidth(myIsm.kBwMedium)

    while True:
      if myIsm.check_status():
        accelData = myIsm.get_accel()
        gyroData = myIsm.get_gyro()
        time.sleep(0.100)
        return accelData, gyroData
try:
  while True:
    imu_reader()
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
    
    



