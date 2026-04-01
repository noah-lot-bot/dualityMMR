from adafruit_servokit import ServoKit
import sshkeyboard

# notes for matthew
kit = ServoKit(channels=16) # creates the board with 16 channels 0-15
kit.servo[int].angle = float #board.servo[position].angle = angle to set number to (limited from 0 to 180)
kit.continuous_servo[int].throttle = float #board.servo[position]."Speed" = speed to set cont servo to (limited -1 to 1)

# i do not know the neutral positions of each servo so we cannot count on those rn, will update later
class leg:
  wheel_stop = # should be constant across all legs
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
front_right_leg = leg()
back_left_leg = leg()
back_right_leg = leg()

# for right now since you do not have the locations you can pull something still with its correct name and we will fill in later
front_left_leg.hip_location # like so , example only

# the first step in the auto gait demo is to set up neutral positions and set wheels to stop (WIP)
kit.servo[front_right_leg.hip_location].angle = front_right_leg.hip_neutral

def flat_ground_gait(): #WIP
  kit.servo[front_left_leg.knee_location].angle = 30
