from adafruit_servokit import ServoKit
import sshkeyboard
import asyncio

# notes for matthew
kit = ServoKit(channels=16) # creates the board with 16 channels 0-15
kit.servo[int].angle = float #board.servo[position].angle = angle to set number to (limited from 0 to 180, no negatives)
kit.continuous_servo[int].throttle = float #board.servo[position]."Speed" = speed to set cont servo to (limited -1 to 1)

# i do not know the neutral positions of each servo so we cannot count on those rn, will update later
class leg:
  wheel_stop = 0.2 # should be constant across all legs
  def __init__(self, hip_location, knee_location, wheel_location, hip_min, hip_max, hip_neutral, knee_min, knee_max, knee_neutral):
    self.hip_location = hip_location
    self.knee_location = knee_location
    self.wheel_location = wheel_location
    self.hip_min = hip_min
    self.hip_max = hip_max
    self.hip_neutral = hip_neutral
    self.knee_min = knee_min
    self.knee_max = knee_max
    self.knee_neutral = knee_neutral

# we are going to hard code the servo locations because its way easier than asking for them
front_left_leg = leg(0,1,2,64,)
front_right_leg = leg(3,4,5)
back_left_leg = leg(6,7,8)
back_right_leg = leg(9,10,11)

# define a function to rotate a servo from an initial to final position, accept negative angles, WIP: SMOOTH MOTION
async def rotate_servo(servo_location, angle, period):
  servo_pos_init = kit.servo[servo_location].angle
  servo_pos_fin = servo_pos_init + angle
  while servo_pos_curr :!= servo_pos_fin # WORK IN PROGRESS
  kit.servo[servo_location].angle = servo_pos_fin

# the first step in the automatic gait demo is to set all legs to their neutral positions
async def set_neutral(): # WIP
  await asyncio.gather(
    kit.servo[front_left_leg.knee_location].angle = front_left_leg.knee_neutral,
    kit.servo[front_left_leg.hip_location].angle = front_left_leg.hip_neutral

async def flat_ground_gait(front_left_leg, front_right_leg, back_left_leg, back_right_leg):
  # front left
  await rotate_servo(front_left_leg.knee_location, 30,)
  await rotate_servo(front_left_leg.hip_location, 40,)
  await rotate_servo(front_left_leg.knee_location, -30,)
  await asyncio.gather( 
    rotate_servo(front_left_leg.hip_location, -10,),
    rotate_servo(back_left_leg.hip_location, -10,),
    rotate_servo(front_right_leg.hip_location, 10,),
    rotate_servo(back_right_leg.hip_location, 10,)
  )
  # back right
  await rotate_servo(back_right_leg.knee_location, 30,)
  await rotate_servo(back_right_leg.hip_location, -40,)
  await rotate_servo(back_right_leg.knee_location, -30,)
  await asyncio.gather( 
    rotate_servo(front_left_leg.hip_location, -10,),
    rotate_servo(back_left_leg.hip_location, -10,),
    rotate_servo(front_right_leg.hip_location, 10,),
    rotate_servo(back_right_leg.hip_location, 10,)
  )
  # front right
  await rotate_servo(front_right_leg.knee_location, 30,)
  await rotate_servo(back_right_leg.hip_location, -40,)
  await rotate_servo(back_right_leg.knee_locationm -30,)
  await asyncio.gather( 
    rotate_servo(front_left_leg.hip_location, -10,),
    rotate_servo(back_left_leg.hip_location, -10,),
    rotate_servo(front_right_leg.hip_location, 10,),
    rotate_servo(back_right_leg.hip_location, 10,)
  )
  # back left
  await rotate_servo(front_right_leg.knee_location, 30,)
  await rotate_servo(back_right_leg.hip_location, -40,)
  await rotate_servo(back_right_leg.knee_location, -30,)
  await asyncio.gather( 
    rotate_servo(front_left_leg.hip_location, -10,),
    rotate_servo(back_left_leg.hip_location, -10,),
    rotate_servo(front_right_leg.hip_location, 10,),
    rotate_servo(back_right_leg.hip_location, 10,)
  )



async def upslope_partial_lower_gait(front_left_leg, front_right_leg, back_left_leg, back_right_leg):
  # front left
  await rotate_servo(front_left_leg.knee_location, 30,)
  await rotate_servo(front_left_leg.hip_location, 40,)
  await rotate_servo(front_left_leg.knee_location, -30,)
  await asyncio.gather( 
    rotate_servo(front_left_leg.hip_location, -10,),
    rotate_servo(back_left_leg.hip_location, -10,),
    rotate_servo(front_right_leg.hip_location, 10,),
    rotate_servo(back_right_leg.hip_location, 10,)
  )
  # lower rear
  await asyncio.gather(
    rotate_servo(back_left_leg.knee_location, 35,), # physical max (TBD)
    rotate_servo(back_right_leg.knee_location, 35,) # physical max (TBD)
  )
  # back right
  await rotate_servo(back_right_leg.hip_location, -40,)
  # raise rear
  await asyncio.gather(
    rotate_servo(back_left_leg.knee_location, -35,), # physical max (TBD)
    rotate_servo(back_right_leg.knee_location, -35,) # physical max (TBD)
  )
  await asyncio.gather( 
    rotate_servo(front_left_leg.hip_location, -10,),
    rotate_servo(back_left_leg.hip_location, -10,),
    rotate_servo(front_right_leg.hip_location, 10,),
    rotate_servo(back_right_leg.hip_location, 10,)
  )
  # front right
  await rotate_servo(front_right_leg.knee_location, 30,)
  await rotate_servo(back_right_leg.hip_location, -40,)
  await rotate_servo(back_right_leg.knee_locationm -30,)
  await asyncio.gather( 
    rotate_servo(front_left_leg.hip_location, -10,),
    rotate_servo(back_left_leg.hip_location, -10,),
    rotate_servo(front_right_leg.hip_location, 10,),
    rotate_servo(back_right_leg.hip_location, 10,)
  )
  # lower rear
  await asyncio.gather(
    rotate_servo(back_left_leg.knee_location, 35,), # physical max (TBD)
    rotate_servo(back_right_leg.knee_location, 35,) # physical max (TBD)
  )
  # back left
  await rotate_servo(back_left_leg.hip_location, -40,)
  # raise rear
  await asyncio.gather(
    rotate_servo(back_left_leg.knee_location, -35,), # physical max (TBD)
    rotate_servo(back_right_leg.knee_location, -35,) # physical max (TBD)
  )
  await asyncio.gather( 
    rotate_servo(front_left_leg.hip_location, -10,),
    rotate_servo(back_left_leg.hip_location, -10,),
    rotate_servo(front_right_leg.hip_location, 10,),
    rotate_servo(back_right_leg.hip_location, 10,)
  )



async def upslope_downslope_full_lower_gait(front_left_leg, front_right_leg, back_left_leg, back_right_leg):
  # lower
  await asyncio.gather( 
    rotate_servo(front_left_leg.knee_location, 35,), # physical max (TBD)
    rotate_servo(back_left_leg.knee_location, 35,), # physical max (TBD)
    rotate_servo(front_right_leg.knee_location, 35,), # physical max (TBD)
    rotate_servo(back_right_leg.knee_location, 35,) # physical max (TBD)
  )
  # front legs
  await asyncio.gather(
    rotate_servo(front_left_leg.hip_location, 40,),
    rotate_servo(front_right_leg.hip_location, -40,)
  )
  # raise and adjust chassis
  await asyncio.gather( 
    rotate_servo(front_left_leg.knee_location, -35,), # physical max (TBD)
    rotate_servo(back_left_leg.knee_location, -35,), # physical max (TBD)
    rotate_servo(front_right_leg.knee_location, -35,), # physical max (TBD)
    rotate_servo(back_right_leg.knee_location, -35,) # physical max (TBD)
    rotate_servo(front_left_leg.hip_location, -20,),
    rotate_servo(back_left_leg.hip_location, -20,),
    rotate_servo(front_right_leg.hip_location, 20,),
    rotate_servo(back_right_leg.hip_location, 20,)
  )
  # lower
  await asyncio.gather( 
    rotate_servo(front_left_leg.knee_location, 35,), # physical max (TBD)
    rotate_servo(back_left_leg.knee_location, 35,), # physical max (TBD)
    rotate_servo(front_right_leg.knee_location, 35,), # physical max (TBD)
    rotate_servo(back_right_leg.knee_location, 35,) # physical max (TBD)
  )
  # rear legs
  await asyncio.gather(
    rotate_servo(back_left_leg.hip_location, 40,),
    rotate_servo(back_right_leg.hip_location, -40,)
  )
  # raise and adjust chassis
  await asyncio.gather( 
    rotate_servo(front_left_leg.knee_location, -35,), # physical max (TBD)
    rotate_servo(back_left_leg.knee_location, -35,), # physical max (TBD)
    rotate_servo(front_right_leg.knee_location, -35,), # physical max (TBD)
    rotate_servo(back_right_leg.knee_location, -35,) # physical max (TBD)
    rotate_servo(front_left_leg.hip_location, -20,),
    rotate_servo(back_left_leg.hip_location, -20,),
    rotate_servo(front_right_leg.hip_location, 20,),
    rotate_servo(back_right_leg.hip_location, 20,)
  )
