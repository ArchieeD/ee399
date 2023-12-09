from pymycobot.mycobot import MyCobot
from pymycobot import PI_PORT,PI_BAUD
import math

print(PI_PORT)
print(PI_BAUD)
mycobot = MyCobot(PI_PORT, PI_BAUD) # Initialize the robot arm for raspberry Pi version
mycobot.release_all_servos()

def print_info():
    print(mycobot.get_angles())
    print(mycobot.get_coords())

mycobot.set_gripper_state(0,50)

while(1):
    input("")
    mycobot.set_gripper_state(1,50)
    print_info()