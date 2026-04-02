from adafruit_servokit import ServoKit
import time
import asyncio

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
    if prog >= 1:
      break
    servo_pos_curr = servo_pos_init + (servo_pos_fin-servo_pos_init)*prog
    kit.servo[location].angle = servo_pos_curr
    await asyncio.sleep(0.02)

servo_inp_loc = int(input("Enter Servo Location: "))
inp_angle = float(input("Enter Change in Angle: "))
inp_period = float(input("Enter target period: "))

async def main():
  servo_inp_loc = int(input("Enter Servo Location: "))
  inp_angle = float(input("Enter Change in Angle: "))
  inp_period = float(input("Enter target period: "))
  await rotate_servo(servo_inp_loc, inp_angle, inp_period)

asyncio.run(main())
  
