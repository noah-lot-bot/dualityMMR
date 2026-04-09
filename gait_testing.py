import asyncio 
from sshkeyboard import listen_keyboard, stop_listening
from gait_definitions import (turn_right_gait, turn_left_gait, set_neutral, front_left_leg, front_right_leg, back_left_leg, back_right_leg, roll_forward_gait, roll_backward_gait, raise_chassis_gait, lower_chassis_gait) 
from telemetry_handler import telemetry_handler

asyncio.run(set_neutral(front_left_leg, front_right_leg, back_left_leg, back_right_leg))
asyncio.run(telemetry_handler)

async def key_pressed(key):
  try: 
    if key == "w":
      await roll_forward_gait(front_left_leg, front_right_leg, back_left_leg, back_right_leg)
    elif key == "s":
      await roll_backward_gait(front_left_leg, front_right_leg, back_left_leg, back_right_leg)
    elif key == "d":
      await turn_right_gait(front_left_leg, front_right_leg, back_left_leg, back_right_leg)
    elif key == "a":
      await turn_left_gait(front_left_leg, front_right_leg, back_left_leg, back_right_leg)
    elif key == "e":
      await raise_chassis_gait(front_left_leg, front_right_leg, back_left_leg, back_right_leg)
    elif key == "q":
      await lower_chassis_gait(front_left_leg, front_right_leg, back_left_leg, back_right_leg)
  except AttributeError:
    if key == "esc":
      await set_neutral(front_left_leg, front_right_leg, back_left_leg, back_right_leg)
      return False

async def key_released(key):
  try: 
    if key == "w":
      await set_neutral(front_left_leg, front_right_leg, back_left_leg, back_right_leg)
    elif key == "s":
      await set_neutral(front_left_leg, front_right_leg, back_left_leg, back_right_leg)
    elif key == "a":
      await set_neutral(front_left_leg, front_right_leg, back_left_leg, back_right_leg)
    elif key == "d":
      await set_neutral(front_left_leg, front_right_leg, back_left_leg, back_right_leg)
  except AttributeError:
    pass 

# start the listener
try:
  listen_keyboard(on_press = key_pressed, on_release = key_released,)
finally:
  asyncio.run(set_neutral(front_left_leg, front_right_leg, back_left_leg, back_right_leg))
