import asyncio 
from sshkeyboard import listen_keyboard_manual, stop_listening
from gait_definitions import (turn_right_gait, turn_left_gait, set_neutral, front_left_leg, front_right_leg, back_left_leg, back_right_leg, roll_forward_gait, roll_backward_gait, raise_chassis_gait, lower_chassis_gait, upslope_gait) 
from telemetry_handler import telemetry_handler

asyncio.run(set_neutral(front_left_leg, front_right_leg, back_left_leg, back_right_leg))
asyncio.run(upslope_gait)
