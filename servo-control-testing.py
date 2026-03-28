# import the servo control library for the pca9685 board (should be downloaded in venv)
from adafruit_servokit import ServoKit

# import the keyboard detection library (should be downloaded in venv)
import keyboard

# establish the board (which has 16 channels)
kit = ServoKit(channels=16)

# ask user for input on servo locations
def servo_locations():
  while True:
    try: 
      w = int(input("Where is the wheel servo? Enter an integer between 0 and 15."))
      if 0<=w<=15:
        break
      print("Error: Servo location must be between 0 and 15.")
    except ValueError:
      print("Error: Servo location must be an integer.")
  while True:
    try: 
      k = int(input('Where is the knee servo? Enter an integer between 0 and 15.'))
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
      h = int(input('Where is the hip servo? Enter an integer between 0 and 15.'))
      if not 0<=h<=15:
        print("Error: Servo location must be between 0 and 15.")
      elif h==w or h==k:
        print("Error: Multple servos cannot occupy the same location.")
      else:
        break
    except ValueError:
      print("Error: Servo location must be an integer.")
  return w, k, h

w, k, h = servo_locations();
print(f"Servo Locations: hip at {h}, wheel at {w}, knee at {k}.")

