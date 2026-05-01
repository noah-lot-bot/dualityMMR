import asyncio 
from sshkeyboard import listen_keyboard_manual, stop_listening
from gait_definitions import *
from telemetry_handler import telemetry_handler

# set neutral is always first step
asyncio.run(initialize_neutral(front_left_leg, front_right_leg, back_left_leg, back_right_leg))

# define what happens on key press
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

# define what happens on key release
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

# start the listener and data collection
async def main():
  await asyncio.gather(listen_keyboard_manual(on_press = key_pressed, on_release = key_released,),
                       telemetry_handler()
                      )

# runs everything once
if __name__=="__main__":
  try:
    asyncio.run(main())
  except KeyboardInterrupt:
    asyncio.run(set_neutral(front_left_leg, front_right_leg, back_left_leg, back_right_leg))
