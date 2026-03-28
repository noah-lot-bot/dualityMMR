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
      w = input("Where is the wheel servo? Enter an integer between 0 and 15.")
      w = int(w)
        if w<0 or w>15
          raise ValueError("Invalid wheel servo location.")
      k = input('Where is the knee servo? Enter an integer between 0 and 15.')
      k = int(k)
        if k<0 or k>15
          raise ValueError("Invalid knee servo location.")
        elif k==w
          raise ValueError("Multiple servos cannot occupy same location.")
      h = input("Where is the hip servo? Enter an integer between 0 and 15.")
      h = int(h)
        if h<0 or h>15
          raise ValueError("Invalid hip servo location.")
        elif h==w or h==k
          raise ValueError("Multiple servos cannot occupy same location.")
      return w, k, h
    except ValueError:
      print("Please correct the invalid input")

locations = servo_locations();
print(f"Servo Locations: hip at {h}, wheel at {w}, knee at {k}.")

