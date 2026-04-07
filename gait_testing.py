import asyncio 
import sshkeyboard
from

def key_pressed(key):
  try: 
    if key == "w":
      
    elif key == "s":
      kit.continuous_servo[wheel_loc].throttle=-1
    elif key == "q":
      if knee_pos <= knee_max:
        knee_pos += 5
        kit.servo[knee_loc].angle = knee_pos
    elif key == "e":
      if knee_pos >= knee_min:
        knee_pos -= 5
        kit.servo[knee_loc].angle = knee_pos
    elif key == "d":
      if hip_pos <= hip_max:
        hip_pos += 5
        kit.servo[hip_loc].angle = hip_pos
    elif key == "a":
      if hip_pos >= hip_min:
        hip_pos -= 5
        kit.servo[hip_loc].angle = hip_pos
  except AttributeError:
    if key == "esc":
      rover_shutdown()
      return False
