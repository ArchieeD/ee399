from pymycobot.mycobot import MyCobot
from pymycobot import PI_PORT,PI_BAUD
import math
import time
import csv
from extract_values import read_csv

mycobot = MyCobot(PI_PORT, PI_BAUD) # Initialize the robot arm for raspberry Pi version
print(mycobot.is_power_on())
coords_list = read_csv('task1position.csv', 'c')

print(len(coords_list))
for i in range(5):
    for coord in coords_list:
        time.sleep(2)
        mycobot.send_angles([0,0,0,0,0,0], 70)
        time.sleep(3)
        input("Press enter to advance to next coords")
        print("current coords: ", coord)
        mycobot.send_coords([coord[0],0,0,0,0,0],50)
        time.sleep(2)
        mycobot.send_coords(coord, 70)
        input("Press enter to advance to home")
        mycobot.send_coords([coord[0],0,0,0,0,0],50)
