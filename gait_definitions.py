from adafruit_servokit import ServoKit
import sshkeyboard
import asyncio
import time
import math

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
front_left_leg = leg(13,14,12, 0,95,21, 59,125,84)
front_right_leg = leg(2,1,0, 40,131,113, 20,90,55)
back_left_leg = leg(11,10,9, 47,140,120, 25,85,60)
back_right_leg = leg(4,5,6, 28,127,48, 60,130,92)

async def movement_restrictor(location, servo_pos_init, servo_pos_curr):
  if location == front_left_leg.hip_location and (servo_pos_curr>front_left_leg.hip_max or servo_pos_curr<front_left_leg.hip_min):
    return servo_pos_init
  elif location == front_right_leg.hip_location and (servo_pos_curr>front_right_leg.hip_max or servo_pos_curr<front_right_leg.hip_min):
    return servo_pos_init
  elif location == back_left_leg.hip_location and (servo_pos_curr>back_left_leg.hip_max or servo_pos_curr<back_left_leg.hip_min):
    return servo_pos_init
  elif location == back_right_leg.hip_location and (servo_pos_curr>back_right_leg.hip_max or servo_pos_curr<back_right_leg.hip_min):
    return servo_pos_init
  elif location == front_left_leg.knee_location and (servo_pos_curr>front_left_leg.knee_max or servo_pos_curr<front_left_leg.knee_min):
    return servo_pos_init
  elif location == front_right_leg.knee_location and (servo_pos_curr>front_right_leg.knee_max or servo_pos_curr<front_right_leg.knee_min):
    return servo_pos_init
  elif location == back_left_leg.knee_location and (servo_pos_curr>back_left_leg.knee_max or servo_pos_curr<back_left_leg.knee_min):
    return servo_pos_init
  elif location == back_right_leg.knee_location and (servo_pos_curr>back_right_leg.knee_max or servo_pos_curr<back_right_leg.knee_min):
    return servo_pos_init
  else:
    return servo_pos_curr

# define a function to rotate a servo from an initial to final position, accept negative angles, smooth motion
async def rotate_servo(location, angle, period):
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
    #servo_pos_curr = await movement_restrictor(location, servo_pos_init, servo_pos_curr)
    kit.servo[location].angle = servo_pos_curr
    await asyncio.sleep(0.02)

async def rotate_servo_absolute(location, angle):
 kit.servo[location].angle = angle

# awaitable wheel speed set
async def set_wheel_speed(wheel_location, speed):
  kit.continuous_servo[wheel_location].throttle = speed

# the first step in the automatic gait demo is to set all legs to their neutral positions
async def set_neutral(front_left_leg, front_right_leg, back_left_leg, back_right_leg): # WIP
  await asyncio.gather(
    set_wheel_speed(front_left_leg.wheel_location, 0.1),
    set_wheel_speed(front_right_leg.wheel_location, 0.1),
    set_wheel_speed(back_left_leg.wheel_location, 0.1),
    set_wheel_speed(back_right_leg.wheel_location, 0.1)
  )
  await asyncio.gather(
    rotate_servo_absolute(front_left_leg.knee_location, front_left_leg.knee_neutral),
    rotate_servo_absolute(front_right_leg.knee_location, front_right_leg.knee_neutral),
    rotate_servo_absolute(back_left_leg.knee_location, back_left_leg.knee_neutral),
    rotate_servo_absolute(back_right_leg.knee_location, back_right_leg.knee_neutral)
  )
  await asyncio.gather(
    rotate_servo_absolute(front_left_leg.hip_location, front_left_leg.hip_neutral),
    rotate_servo_absolute(front_right_leg.hip_location, front_right_leg.hip_neutral),
    rotate_servo_absolute(back_left_leg.hip_location, back_left_leg.hip_neutral),
    rotate_servo_absolute(back_right_leg.hip_location, back_right_leg.hip_neutral)
  )

# define the safe shutdown function (WIP)
async def wait_for_user():
    """Allows telemetry to continue while motion waits for Enter."""
    loop = asyncio.get_running_loop()
    print("\n[PAUSED] Press Enter to execute next step...")
    await loop.run_in_executor(None, input)

async def upslope_gait(front_left_leg, front_right_leg, back_left_leg, back_right_leg):
  # back left crawl
  await set_wheel_speed(back_right_leg.wheel_location, 0.5)
  await rotate_servo(back_right_leg.hip_location, back_right_leg.hip_max-back_right_leg.hip_neutral, 3)
  await set_wheel_speed(back_right_leg.wheel_location, 0.1)
  
  await rotate_servo(back_left_leg.knee_location, back_left_leg.knee_neutral-back_left_leg.knee_max, 2)
  await rotate_servo(back_left_leg.hip_location, back_left_leg.hip_max-back_left_leg.hip_neutral, 2)
  await rotate_servo(back_left_leg.knee_location, back_left_leg.knee_max-back_left_leg.knee_neutral, 2)
  
  await set_wheel_speed(back_left_leg.wheel_location, -0.5)
  await rotate_servo(back_left_leg.hip_location, back_left_leg.hip_neutral-back_left_leg.hip_max, 2)
  await set_wheel_speed(back_left_leg.wheel_location, 0.1)
  
  await set_wheel_speed(back_right_leg.wheel_location, -0.5)
  await rotate_servo(back_right_leg.hip_location, back_right_leg.hip_neutral-back_right_leg.hip_max, 3)
  await set_wheel_speed(back_right_leg.wheel_location, 0.1)

  # front left crawl
  await set_wheel_speed(front_right_leg.wheel_location, -0.5)
  await rotate_servo(front_right_leg.hip_location, front_right_leg.hip_min-front_right_leg.hip_neutral, 3) 
  await set_wheel_speed(front_right_leg.wheel_location, 0.1)
  
  await rotate_servo(front_left_leg.knee_location, front_left_leg.knee_max-front_left_leg.knee_neutral, 2)
  await rotate_servo(front_left_leg.hip_location, front_left_leg.hip_max-front_left_leg.hip_neutral, 2)
  await rotate_servo(front_left_leg.knee_location, front_left_leg.knee_neutral-front_left_leg.knee_max, 2)
  
  await set_wheel_speed(front_left_leg.wheel_location, -0.5)
  await rotate_servo(front_left_leg.hip_location, front_left_leg.hip_neutral-front_left_leg.hip_max, 2)
  await set_wheel_speed(front_left_leg.wheel_location, 0.1)

  await set_wheel_speed(front_right_leg.wheel_location, 0.5)
  await rotate_servo(front_right_leg.hip_location, front_right_leg.hip_neutral-front_right_leg.hip_min, 3)
  await set_wheel_speed(front_right_leg.wheel_location, 0.1)

  # back right crawl
  await set_wheel_speed(back_left_leg.wheel_location, -0.5)
  await rotate_servo(back_left_leg.hip_location, back_left_leg.hip_min-back_left_leg.hip_neutral, 3) 
  await set_wheel_speed(back_left_leg.wheel_location, 0.1)
  
  await rotate_servo(back_right_leg.knee_location, back_right_leg.knee_max-back_right_leg.knee_neutral, 2) #too far
  await rotate_servo(back_right_leg.hip_location, back_right_leg.hip_min-back_right_leg.hip_neutral, 2) #!!! too far
  await rotate_servo(back_right_leg.knee_location, back_right_leg.knee_neutral-back_right_leg.knee_max, 2)
  await set_wheel_speed(back_right_leg.wheel_location, 0.5)
  await rotate_servo(back_right_leg.hip_location, back_right_leg.hip_neutral-back_right_leg.hip_min, 2)
  await set_wheel_speed(back_right_leg.wheel_location, 0.1)

  await set_wheel_speed(back_left_leg.wheel_location, 0.5)
  await rotate_servo(back_left_leg.hip_location, back_left_leg.hip_neutral-back_left_leg.hip_min, 3)
  await set_wheel_speed(back_left_leg.wheel_location, 0.1)

  # front right crawl
  await set_wheel_speed(front_left_leg.wheel_location, 0.5)
  await rotate_servo(front_left_leg.hip_location, front_right_leg.hip_neutral-front_right_leg.hip_min, 3)
  await set_wheel_speed(front_left_leg.wheel_location, 0.1)
  
  await rotate_servo(front_right_leg.knee_location, front_right_leg.knee_min-front_right_leg.knee_neutral, 2) #!!!
  await rotate_servo(front_right_leg.hip_location, front_right_leg.hip_min-front_right_leg.hip_neutral, 2)
  await rotate_servo(front_right_leg.knee_location, front_right_leg.knee_neutral-front_right_leg.knee_min, 2)
  await set_wheel_speed(front_right_leg.wheel_location, 0.5)
  await rotate_servo(front_right_leg.hip_location, front_right_leg.hip_neutral-front_right_leg.hip_min, 2) 
  await set_wheel_speed(front_right_leg.wheel_location, 0.1)

  await set_wheel_speed(front_left_leg.wheel_location, -0.5)
  await rotate_servo(front_left_leg.hip_location, front_left_leg.hip_neutral-front_left_leg.hip_max, 3)
  await set_wheel_speed(front_left_leg.wheel_location, 0.1)

async def turn_right_gait(front_left_leg, front_right_leg, back_left_leg, back_right_leg):
  await asyncio.gather(
    set_wheel_speed(front_left_leg.wheel_location, 1),
    set_wheel_speed(back_left_leg.wheel_location, 1),
    set_wheel_speed(front_right_leg.wheel_location, 1),
    set_wheel_speed(back_right_leg.wheel_location, 1)
  )

async def turn_left_gait(front_left_leg, front_right_leg, back_left_leg, back_right_leg):
  await asyncio.gather(
    set_wheel_speed(front_left_leg.wheel_location, -1),
    set_wheel_speed(back_left_leg.wheel_location, -1),
    set_wheel_speed(front_right_leg.wheel_location, -1),
    set_wheel_speed(back_right_leg.wheel_location, -1)
  )

async def roll_forward_gait(front_left_leg, front_right_leg, back_left_leg, back_right_leg):
  await asyncio.gather(
    set_wheel_speed(front_left_leg.wheel_location, 1),
    set_wheel_speed(back_left_leg.wheel_location, 1),
    set_wheel_speed(front_right_leg.wheel_location, -1),
    set_wheel_speed(back_right_leg.wheel_location, -1)
)

async def roll_backward_gait(front_left_leg, front_right_leg, back_left_leg, back_right_leg):
  await asyncio.gather(
    set_wheel_speed(front_left_leg.wheel_location, -1),
    set_wheel_speed(back_left_leg.wheel_location, -1),
    set_wheel_speed(front_right_leg.wheel_location, 1),
    set_wheel_speed(back_right_leg.wheel_location, 1)
)

async def raise_chassis_gait(front_left_leg, front_right_leg, back_left_leg, back_right_leg):
  await asyncio.gather(
    rotate_servo(front_left_leg.knee_location, 5, 1),
    rotate_servo(back_right_leg.knee_location, 5, 1)
)

async def lower_chassis_gait(front_left_leg, front_right_leg, back_left_leg, back_right_leg):
  await asyncio.gather(
    rotate_servo(front_left_leg.knee_location, -5, 1),
    rotate_servo(back_right_leg.knee_location, -5, 1)
)
    

