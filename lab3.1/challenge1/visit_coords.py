from pymycobot.mycobot import MyCobot
from pymycobot import PI_PORT,PI_BAUD
import math
import time
import csv
from extract_values import read_csv

mycobot = MyCobot(PI_PORT, PI_BAUD) # Initialize the robot arm for raspberry Pi version
print(mycobot.is_power_on())

# Read coordinates and angles from csv files 
coords_list = read_csv('task1position.csv', 'c')
angles_list = read_csv('task1position.csv', 'a')
hammer_coords_list = read_csv('hammerlocation.csv', 'c')
hammer_angles_list = read_csv('hammerlocation.csv', 'a')

# Extract the initial block pickup coordinates and angle 
block_pickup_coord = coords_list[0]
block_pickup_angle = angles_list[0]

# Remove the initial coordinate and angle from the lists 
coords_list = coords_list[1:]
angles_list = angles_list[1:]


# Function to move the robot to a specified position 
def find_pos(mycobot, coords, angles, adjustHeight, is_pickup_loc=False):
    x = coords[0]
    y = coords[1]
    z = coords[2]
    rx = coords[3]
    ry = coords[4]
    rz = coords[5]
    mycobot.send_angles([angles[0],0,0,0,0,0], 50)
    time.sleep(2)
    mycobot.send_coords([x,y,z+adjustHeight, rx, ry, rz], 50)
    time.sleep(2)
    while True:
        modify_pos = int(input(""))
        if modify_pos == 0:
            break
        elif modify_pos == 1: # rotate left
            if y < 0:
                x += 3
                y += 3
            else:
                x -= 3
                y += 3
        elif modify_pos == 2: # rotate right
            if y < 0:
                x -= 3
                y -= 3
            else:
                x += 3
                y -= 3
        elif modify_pos == 3: # move forward
            x += 3
            if y < 0:
                y -= 3
            else :
                y += 3
        elif modify_pos == 4: # move back 
            x -= 3
            if y < 0:
                y += 3
            else:
                y -= 3

        mycobot.send_coords([x,y,z+adjustHeight, rx, ry, rz], 10)
        time.sleep(2)
    mycobot.send_coords([x,y,z-5, rx, ry, rz], 30)
    time.sleep(2)
    if is_pickup_loc:
        mycobot.set_gripper_state(1,50)
        time.sleep(2)
        mycobot.set_gripper_state(1,50)
        time.sleep(2)
        mycobot.set_gripper_state(1,50)
        time.sleep(1)
        mycobot.set_gripper_state(1,50)
        time.sleep(1)
    else:
        mycobot.set_gripper_state(0,50)
        time.sleep(2)
        mycobot.set_gripper_state(0,50)
        time.sleep(2)
        mycobot.set_gripper_state(0,50)
        time.sleep(1)
        mycobot.set_gripper_state(0,50)
        time.sleep(1)

    mycobot.send_angles([angles[0],0,0,0,0,0], 30)
    time.sleep(3)

mycobot.send_angles([0,0,0,0,0,0], 50)
time.sleep(2)
mycobot.set_gripper_state(0,50)
time.sleep(2)
mycobot.set_gripper_state(0,50)
time.sleep(1)
mycobot.set_gripper_state(0,50)
time.sleep(1)


print("Press 0 if finished, 1 to rotate left, 2 to rotate right, 3 to move forward, and 4 to move back:")
for i in range(len(coords_list)):
    find_pos(mycobot, block_pickup_coord, block_pickup_angle,15, True)
    time.sleep(1)
    find_pos(mycobot, coords_list[i], angles_list[i], 15)
    mycobot.set_gripper_state(0,50)
    time.sleep(1)
    
# Extract the initial hammer pickup coordinates and angle 
hammer_pickup_coord = hammer_coords_list[0]  
hammer_pickup_angle = hammer_angles_list[0]  


find_pos(mycobot, hammer_pickup_coord, hammer_pickup_angle, 15, True)
time.sleep(1)

for i in range(len(coords_list)):
    find_pos(mycobot, coords_list[len(coords_list)-1-i], angles_list[len(coords_list)-1-i], 80, True)
    time.sleep(1)
    redo = input("Press r to redo")
    if redo == 'r':
        find_pos(mycobot, coords_list[len(coords_list)-1-i], angles_list[len(coords_list)-1-i], 80, True)
        time.sleep(1)