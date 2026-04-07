import asyncio 
import sshkeyboard
from gait_definitions import flat_ground_gait, turn_right_gait, turn_left_gait, set_neutral 

def key_pressed(key):
  try: 
    if key == "w":
      flat_ground_gait()
    elif key == "d":
      turn_right_gait()
    elif key == "a":
      turn_left_gait()
  except AttributeError:
    if key == "esc":
      rover_shutdown()
      return False

def key_released(key):
  global walk_forward, walk_backward, knee_up, knee_down, hip_forward, hip_backward
  try: 
    if key == "w":
      set_neutral()
    elif key == "s":
      set_neutral()
    elif key == "a"
      set_neutral()
    elif key == "d":
      set_neutral()
  except AttributeError:
    pass 

# start the listener
try:
  listen_keyboard(on_press = key_pressed, on_release = key_released,)
finally:
  rover_shutdown()
