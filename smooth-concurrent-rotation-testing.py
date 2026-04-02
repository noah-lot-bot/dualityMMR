from adafruit_servokit import ServoKit
import time
import asyncio
import math

kit = ServoKit(channels=16)
kit.servo[0].angle = 60
kit.servo[1].angle = 90
async def rotate_servo(location, angle, period):
  servo_pos_init = kit.servo[location].angle
  servo_pos_fin = servo_pos_init + angle
  time_init = time.time()
  while True:
    time_elapsed = time.time()-time_init
    prog = time_elapsed/period
    smooth_prog = (1-math.cos(prog*math.pi))/2
    if prog >= 1:
      break
    servo_pos_curr = servo_pos_init + (servo_pos_fin-servo_pos_init)*prog
    kit.servo[location].angle = servo_pos_curr
    await asyncio.sleep(0.02)

async def main():
  servo_inp_loc_1 = int(input("Enter Servo Location: "))
  inp_angle_1 = float(input("Enter Change in Angle: "))
  inp_period_1 = float(input("Enter target period: "))
  servo_inp_loc_2 = int(input("Enter Servo Location: "))
  inp_angle_2 = float(input("Enter Change in Angle: "))
  inp_period_2 = float(input("Enter target period: "))
  asycio.gather(
    rotate_servo(servo_inp_loc_1, inp_angle_1, inp_period_1),
    rotate_servo(servo_inp_loc_2, inp_angle_2, inp_period_2)
  )
    

asyncio.run(main())
  
