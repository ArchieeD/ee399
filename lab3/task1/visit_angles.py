from pymycobot.mycobot import MyCobot
from pymycobot import PI_PORT,PI_BAUD
import math
import time
import csv
from extract_values import read_csv

mycobot = MyCobot(PI_PORT, PI_BAUD) # Initialize the robot arm for raspberry Pi version
print(mycobot.is_power_on())
joint_angles_list = read_csv('task1position.csv', 'a')

print(len(joint_angles_list))
for i in range(5):
    for angles in joint_angles_list:
        time.sleep(3)
        mycobot.send_angles([0,0,0,0,0,0], 70)
        time.sleep(3)
        input("Press enter to advance to next angle")
        print("current angles: ", angles)
        mycobot.send_angles([angles[0],0,0,0,0,0], 50)
        time.sleep(2)
        mycobot.send_angles(angles, 70)
        input("Press enter to advance to home")
        mycobot.send_angles([angles[0],0,0,0,0,0], 50)

time.sleep(3)
mycobot.send_angles([0,0,0,0,0,0], 70)
