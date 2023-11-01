from pymycobot import MyCobotSocket
import math
import time
import csv
from extract_values import read_csv

mycobot = MyCobotSocket("10.42.0.116", 9000)
mycobot.connect()
print(mycobot.is_power_on())
coords_list = read_csv('values.csv', 'c')

print(len(coords_list))
for i in range(5):
    for coord in coords_list:
        time.sleep(2)
        mycobot.send_angles([0,0,0,0,0,0], 70)
        time.sleep(3)
        raw_input("Press enter to advance to next coords")
        print("current coords: ", coord)
        mycobot.send_coords(coord, 70)
        raw_input("Press enter to advance to home")
