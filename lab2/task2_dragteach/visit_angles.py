from pymycobot import MyCobotSocket

import math
import time
import csv
from extract_values import read_csv

# Use port 9000 by default
# Replace "192.168.10.22" with the IP address of the robot arm
mycobot = MyCobotSocket("10.42.0.116", 9000)
mycobot.connect()
print(mycobot.is_power_on())
joint_angles_list = read_csv('points.csv', 'a')

print(len(joint_angles_list))
for i in range(5):
    for angles in joint_angles_list:
        time.sleep(3)
        mycobot.send_angles([0,0,0,0,0,0], 70)
        time.sleep(3)
        raw_input("Press enter to advance to next angle")
        print("current angles: ", angles)
        mycobot.send_angles(angles, 70)
        raw_input("Press enter to advance to home")

time.sleep(3)
mycobot.send_angles([0,0,0,0,0,0], 70)
