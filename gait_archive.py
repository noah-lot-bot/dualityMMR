
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

async def upslope_gait(front_left_leg, front_right_leg, back_left_leg, back_right_leg):
  # back left crawl
  await set_wheel_speed(back_right_leg.wheel_location, 0.5)
  await rotate_servo(back_right_leg.hip_location, (back_right_leg.hip_max-back_right_leg.hip_neutral)/2, 3)
  await set_wheel_speed(back_right_leg.wheel_location, 0.1)
  
  await rotate_servo(back_left_leg.knee_location, back_left_leg.knee_neutral-back_left_leg.knee_max, 2)
  await rotate_servo(back_left_leg.hip_location, back_left_leg.hip_max-back_left_leg.hip_neutral, 2)
  await rotate_servo(back_left_leg.knee_location, back_left_leg.knee_max-back_left_leg.knee_neutral, 2)
  
  await rotate_servo(back_left_leg.hip_location, back_left_leg.hip_neutral-back_left_leg.hip_max, 2)
  
  await set_wheel_speed(back_right_leg.wheel_location, -0.5)
  await rotate_servo(back_right_leg.hip_location, (back_right_leg.hip_neutral-back_right_leg.hip_max)/2, 3)
  await set_wheel_speed(back_right_leg.wheel_location, 0.1)

  # front left crawl
  await set_wheel_speed(front_right_leg.wheel_location, -0.5)
  await rotate_servo(front_right_leg.hip_location, (front_right_leg.hip_min-front_right_leg.hip_neutral)/2, 3) 
  await set_wheel_speed(front_right_leg.wheel_location, 0.1)
  
  await rotate_servo(front_left_leg.knee_location, front_left_leg.knee_max-front_left_leg.knee_neutral, 2)
  await rotate_servo(front_left_leg.hip_location, front_left_leg.hip_max-front_left_leg.hip_neutral, 2)
  await rotate_servo(front_left_leg.knee_location, front_left_leg.knee_neutral-front_left_leg.knee_max, 2)
  
  await rotate_servo(front_left_leg.hip_location, front_left_leg.hip_neutral-front_left_leg.hip_max, 2)

  await set_wheel_speed(front_right_leg.wheel_location, 0.5)
  await rotate_servo(front_right_leg.hip_location, (front_right_leg.hip_neutral-front_right_leg.hip_min)/2, 3)
  await set_wheel_speed(front_right_leg.wheel_location, 0.1)

  # back right crawl
  await set_wheel_speed(back_left_leg.wheel_location, -0.5)
  await rotate_servo(back_left_leg.hip_location, (back_left_leg.hip_min-back_left_leg.hip_neutral)/2, 3) 
  await set_wheel_speed(back_left_leg.wheel_location, 0.1)
  
  await rotate_servo(back_right_leg.knee_location, back_right_leg.knee_max-back_right_leg.knee_neutral, 2) #too far
  await rotate_servo(back_right_leg.hip_location, back_right_leg.hip_min-back_right_leg.hip_neutral, 2) #!!! too far
  await rotate_servo(back_right_leg.knee_location, back_right_leg.knee_neutral-back_right_leg.knee_max, 2)
  
  await rotate_servo(back_right_leg.hip_location, back_right_leg.hip_neutral-back_right_leg.hip_min, 2)

  await set_wheel_speed(back_left_leg.wheel_location, 0.5)
  await rotate_servo(back_left_leg.hip_location, (back_left_leg.hip_neutral-back_left_leg.hip_min)/2, 3)
  await set_wheel_speed(back_left_leg.wheel_location, 0.1)

  # front right crawl
  await set_wheel_speed(front_left_leg.wheel_location, 0.5)
  await rotate_servo(front_left_leg.hip_location, (front_right_leg.hip_neutral-front_right_leg.hip_min)/2, 3)
  await set_wheel_speed(front_left_leg.wheel_location, 0.1)
  
  await rotate_servo(front_right_leg.knee_location, front_right_leg.knee_min-front_right_leg.knee_neutral, 2) #!!!
  await rotate_servo(front_right_leg.hip_location, front_right_leg.hip_min-front_right_leg.hip_neutral, 2)
  await rotate_servo(front_right_leg.knee_location, front_right_leg.knee_neutral-front_right_leg.knee_min, 2)
  
  await rotate_servo(front_right_leg.hip_location, front_right_leg.hip_neutral-front_right_leg.hip_min, 2) 

  await set_wheel_speed(front_left_leg.wheel_location, -0.5)
  await rotate_servo(front_left_leg.hip_location, (front_left_leg.hip_neutral-front_left_leg.hip_max)/2, 3)
  await set_wheel_speed(front_left_leg.wheel_location, 0.1)
