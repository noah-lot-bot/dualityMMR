import asyncio 
import sshkeyboard
from gait_definitions import flat_ground_gait, turn_right_gait, turn_left_gait

def key_pressed(key):
  try: 
    if key == "w":
      flat_ground_gait():
    elif key == "d":
      turn_right_gait():
    elif key == "a":
      turn_left_gait():
  except AttributeError:
    if key == "esc":
      rover_shutdown()
      return False
