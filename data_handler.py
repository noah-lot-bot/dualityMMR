import qwiic_ism330dhcx
  
def imu_reader():
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

  if myIsm.check_status():
    accelData = myIsm.get_accel()
    gyroData = myIsm.get_gyro()
    time.sleep(0.100)
    return accelData, gyroData
