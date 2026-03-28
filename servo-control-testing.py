# import the servo control library for the pca9685 board
from adafruit_servokit import ServoKit

# import the keyboard detection library 
import keyboard

# import timelibrary
import time

# establish the board (which has 16 channels)
kit = ServoKit(channels=16)

# ask user for input on servo locations
def servo_locations():
  while True:
    try: 
      w = int(input("Where is the wheel servo? Enter an integer between 0 and 15. "))
      if 0<=w<=15:
        break
      print("Error: Servo location must be between 0 and 15.")
    except ValueError:
      print("Error: Servo location must be an integer.")
  while True:
    try: 
      k = int(input('Where is the knee servo? Enter an integer between 0 and 15. '))
      if not 0<=k<=15:
        print("Error: Servo location must be between 0 and 15.")
      elif k==w:
        print("Error: Multiple servos cannot occupy the same location.")
      else:
        break
    except ValueError:
      print("Error: Servo location must be an integer.")
  while True:
    try:
      h = int(input('Where is the hip servo? Enter an integer between 0 and 15. '))
      if not 0<=h<=15:
        print("Error: Servo location must be between 0 and 15.")
      elif h==w or h==k:
        print("Error: Multple servos cannot occupy the same location.")
      else:
        break
    except ValueError:
      print("Error: Servo location must be an integer.")
  return w, k, h

# pull the defined servo locations
wheel_loc, knee_loc, hip_loc = servo_locations();

def rover_shutdown():
  print("Shutting down test...")
  kit.continuous_servo[wheel_loc].throttle=0
  kit.servo[hip_loc].angle=0
  kit.servo[knee_loc].angle=20
  time.sleep(1)
  kit.servo[hip_loc].angle=None
  kit.servo[knee_loc].angle=None
  print("System shut down")

try: 
  while True: 
    if keyboard.is_pressed('w'):
      kit.continuous_servo[wheel_loc].throttle=1
    elif keyboard.is_pressed('s'):
      kit.continuous_servo[wheel_loc].throttle=-1
    else:
      kit.continuous_servo[wheel_loc].throttle=0
  if keyboard.is_pressed('esc'):
    rover_shutdown()
    time.sleep(0.1)
except Exception:
  print("Error has occured.")
  rover_shutdown()
  
#hipmax  = 30
#hip neutrla 0
#neutralknee=20
#kneemax = 50


