from adafruit_servokit import ServoKit
import sshkeyboard
import asyncio

# establish the pwm board
kit = ServoKit(channels=16)

# i do not know the neutral positions of each servo so we cannot count on those rn, will update later
class leg:
  wheel_stop = 0.1 # should be constant across all legs (WIP)
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

# we are going to hard code the servo locations because its way easier than asking for them (WIP)
front_left_leg = leg(13,14,12, 0,95,21, 60,130,85)
front_right_leg = leg(2,1,0, 45,142,124, 0,0,0)
back_left_leg = leg(11,10,9, 30,120,105, 70,133,107)
back_right_leg = leg(4,5,6, 28,127,48, 60,135,92)

# define a function to rotate a servo from an initial to final position, accept negative angles, smooth motion
async def rotate_servo(servo_location, angle, period):
  servo_pos_init = kit.servo[location].angle
  servo_pos_fin = servo_pos_init + angle
  time_init = time.time()
  while True:
    time_elapsed = time.time()-time_init
    progress = time_elapsed/period
    s_curve = (1-math.cos(progress*math.pi))/2
    if progress >= 1:
      break
    servo_pos_curr = servo_pos_init + (servo_pos_fin-servo_pos_init)*s_curve
    kit.servo[location].angle = servo_pos_curr
    await asyncio.sleep(0.02)

# awaitable wheel speed set
async def set_wheel_speed(wheel_location, speed):
  kit.continuous_servo[wheel_location].throttle = speed

# the first step in the automatic gait demo is to set all legs to their neutral positions
async def set_neutral(): # WIP
  await asyncio.gather(
    rotate_servo(front_left_leg.hip_location, front_left_leg.hip_neutral),
    rotate_servo(front_right_leg.hip_location, front_right_leg.hip_neutral),
    rotate_servo(back_left_leg.hip_location, back_left_leg.hip_neutral),
    rotate_servo(back_right_leg.hip_location, back_right_leg.hip_neutral)
  )
  await asyncio.gather(
    rotate_servo(front_left_leg.knee_location, front_left_leg.knee_neutral),
    rotate_servo(front_right_leg.knee_location, front_right_leg.knee_neutral),
    rotate_servo(back_left_leg.knee_location, back_left_leg.knee_neutral),
    rotate_servo(back_right_leg.knee_location, back_right_leg.knee_neutral)
  )

# define the safe shutdown function (WIP)

async def flat_ground_gait(front_left_leg, front_right_leg, back_left_leg, back_right_leg):
  # WIP : tune period values to make gait faster. This is x8 slower than the speed the gait should go to make prototype rover move at 0.02 m/s, so full rover would go 0.08 m/s
  # front left
  await rotate_servo(front_left_leg.knee_location, 30, 2)
  await asyncio.gather(
    rotate_servo(front_left_leg.hip_location, 30, 3),
    rotate_servo(front_left_leg.knee_location, -30, 4)
  )
  await asyncio.gather( 
    rotate_servo(front_left_leg.hip_location, -7.5, 4),
    rotate_servo(back_left_leg.hip_location, -7.5, 4),
    rotate_servo(front_right_leg.hip_location, 7.5, 4),
    rotate_servo(back_right_leg.hip_location, 7.5, 4)
  )
  # back right
  await rotate_servo(back_right_leg.knee_location, 30, 2)
  await asyncio.gather(
    rotate_servo(front_left_leg.hip_location, 30, 3),
    rotate_servo(front_left_leg.knee_location, -30, 4)
  )
  await asyncio.gather( 
    rotate_servo(front_left_leg.hip_location, -7.5, 4),
    rotate_servo(back_left_leg.hip_location, -7.5, 4),
    rotate_servo(front_right_leg.hip_location, 7.5, 4),
    rotate_servo(back_right_leg.hip_location, 7.5, 4)
  )
  # front right
  await rotate_servo(front_right_leg.knee_location, 30, 2)
  await asyncio.gather(
    rotate_servo(front_left_leg.hip_location, 30, 3),
    rotate_servo(front_left_leg.knee_location, -30, 4)
  )
  await asyncio.gather( 
    rotate_servo(front_left_leg.hip_location, -7.5, 4),
    rotate_servo(back_left_leg.hip_location, -7.5, 4),
    rotate_servo(front_right_leg.hip_location, 7.5, 4),
    rotate_servo(back_right_leg.hip_location, 7.5, 4)
  )
  # back left
  await rotate_servo(front_right_leg.knee_location, 30, 2)
  await asyncio.gather(
    rotate_servo(front_left_leg.hip_location, 30, 3),
    rotate_servo(front_left_leg.knee_location, -30, 4)
  )
  await asyncio.gather( 
    rotate_servo(front_left_leg.hip_location, -7.5, 4),
    rotate_servo(back_left_leg.hip_location, -7.5, 4),
    rotate_servo(front_right_leg.hip_location, 7.5, 4),
    rotate_servo(back_right_leg.hip_location, 7.5, 4)
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
    rotate_servo(back_right_leg.knee_location, -35,), # physical max (TBD)
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
    rotate_servo(back_right_leg.knee_location, -35,), # physical max (TBD)
    rotate_servo(front_left_leg.hip_location, -20,),
    rotate_servo(back_left_leg.hip_location, -20,),
    rotate_servo(front_right_leg.hip_location, 20,),
    rotate_servo(back_right_leg.hip_location, 20,)
  )

async def turn_right_gait(front_left_leg, front_right_leg, back_left_leg, back_right_leg):
  await asyncio.gather(
    set_wheel_speed(front_left_leg.wheel_location, 1),
    set_wheel_speed(back_left_leg.wheel_location, 1),
    set_wheel_speed(front_right_leg.wheel_location, -1),
    set_wheel_speed(back_right_leg.wheel_location, -1)
  )

async def turn_left_gait(front_left_leg, front_right_leg, back_left_leg, back_right_leg):
  await asyncio.gather(
    set_wheel_speed(front_left_leg.wheel_location, -1),
    set_wheel_speed(back_left_leg.wheel_location, -1),
    set_wheel_speed(front_right_leg.wheel_location, 1),
    set_wheel_speed(back_right_leg.wheel_location, 1)
  )

async def roll_forward_gait(front_left_leg, front_right_leg, back_left_leg, back_right_leg):
  await asyncio.gather(
    set_wheel_speed(front_left_leg.wheel_location, 1),
    set_wheel_speed(back_left_leg.wheel_location, 1),
    set_wheel_speed(front_right_leg.wheel_location, 1),
    set_wheel_speed(back_right_leg.wheel_location, 1)
)

