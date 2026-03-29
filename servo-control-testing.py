# import the servo control library for the pca9685 board
from adafruit_servokit import ServoKit

# import the keyboard detection library 
from pynput import keyboard

# import timelibrary
import time

# define some global variables
hip_min, hip_max, hip_neutral = 20, 115, 68
knee_min, knee_max, knee_neutral = 60, 130, 95
wheel_stop = 0.2

walk_forward, walk_backward = False, False
knee_up, knee_down = False, False
hip_forward, hip_backward = False, False


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
wheel_loc, knee_loc, hip_loc = servo_locations()

# start the servos at their neutral positions
kit.servo[knee_loc].angle = knee_neutral
kit.servo[hip_loc].angle = hip_neutral
kit.continuous_servo[wheel_loc].throttle = 0.2

# create position tracker variables
knee_pos = knee_neutral
hip_pos = hip_neutral
wheel_speed = 0.2

# define safe shutdown procedure 
def rover_shutdown():
  print("Shutting down test...")
  kit.continuous_servo[wheel_loc].throttle = 0
  kit.servo[hip_loc].angle = hip_neutral
  kit.servo[knee_loc].angle = knee_neutral
  time.sleep(1)
  kit.servo[hip_loc].angle = None
  kit.servo[knee_loc].angle = None
  kit.continuous_servo[wheel_loc].throttle = 0.2
  listener.stop()
  listener.join()
  print("System shut down.")
  
# define keyboard listeners using pynput
def key_pressed(key):
  global walk_forward, walk_backward, knee_up, knee_down, hip_forward, hip_backward
  try: 
    if key.char=="w":
      walk_forward == True
    elif key.char=="s":
      walk_forward == True
    elif key.char == "e":
      knee_up == True
    elif key.char == "q":
      knee_down == True
    elif key.char == "d":
      hip_forward == True
    elif key.char == "a":
      hip_backward == True
  except AttributeError:
    if key == keyboard.Key.esc:
      rover_shutdown()
      return False

def key_released(key):
  global walk_forward, walk_backward, knee_up, knee_down, hip_forward, hip_backward
  try: 
    if key.char=="w":
      walk_forward == False
    elif key.char=="s":
      walk_forward == False
    elif key.char == "e":
      knee_up == False
    elif key.char == "q":
      knee_down == False
    elif key.char == "d":
      hip_forward == False
    elif key.char == "a":
      hip_backward == False
  except AttributeError:
    pass 

# start the listener
listener = keyboard.Listener(on_press = key_pressed, on_release = key_released)
listener.start()

# command the servos
try:
  while True: 
    if walk_forward:
      kit.continuous_servo[wheel_loc].throttle=1
    elif walk_backward: 
      kit.continuous_servo[wheel_loc].throttle=-1
    elif not (walk_forward or walk_backward)
      kit.continuous_servo[wheel_loc].throttle=0.2
    if knee_up:
      if knee_pos <= knee_max
        knee_pos += 1
        kit.servo[knee_loc].angle = knee_pos
    elif knee_down:
      if knee_pos >= knee_min
        knee_pos -= 1
        kit.servo[knee_loc].angle = knee_pos
    elif not (knee_down or knee_up):
      pass
    if hip_forward:
      if hip_pos <= hip_max
        hip_pos += 1
        kit_servo[hip_loc].angle = hip_pos
    elif hip_backward: 
      if hip_pos >= hip_min
        hip_pos -= 1
        kit.servo[hip_loc].angle = hip_pos
    elif not (hip_forward or hip_backward):
      pass
    time.sleep(1)
except KeyboardInterrupt:
  rover_shutdown()
        
    
# command the servos by checking for green flags

