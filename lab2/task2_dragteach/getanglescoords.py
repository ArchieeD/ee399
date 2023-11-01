from pymycobot import MyCobotSocket
import math
# Use port 9000 by default
# Replace "192.168.10.22" with the IP address of the robot arm
mycobot = MyCobotSocket("10.42.0.116", 9000)
mycobot.connect()
mycobot.release_all_servos()

def print_info():
    print(mycobot.get_angles())
    print(mycobot.get_coords())

for i in range(0,15):
    raw_input()
    print_info()
