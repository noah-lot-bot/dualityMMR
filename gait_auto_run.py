import asyncio 
from sshkeyboard import listen_keyboard_manual, stop_listening
from gait_definitions import *
from telemetry_handler import telemetry_handler

async def main():
  await initialize_neutral(front_left_leg, front_right_leg, back_left_leg, back_right_leg)
  while True:
    await turtle_gait_fix(front_left_leg, front_right_leg, back_left_leg, back_right_leg)
  
if __name__=="__main__":
  try:
    asyncio.run(main())
  except KeyboardInterrupt:
    asyncio.run(set_neutral(front_left_leg, front_right_leg, back_left_leg, back_right_leg))
