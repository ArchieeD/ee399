from pymycobot import MyCobotSocket
import time
import numpy as np

# Use port 9000 by default
mc3 = MyCobotSocket("10.42.0.73", 9000)
mc3.connect()
mc6 = MyCobotSocket("10.42.0.60", 9000)
mc6.connect()

slow_s = 2.5 # seconds
fast_s = 0.5 # seconds
move_fast = 40
move_slow = 10
g_closed = 75
g_open = 101
speed = 60

def goto_Home(mc):
    mc.send_angles([-4.74, 0.87, -90.52, 0.17, 12.12, 2.46], move_fast)
    time.sleep(slow_s)

def goto_Grab(mc, pick, hover):
    while mc.get_gripper_value() < 95:
        mc.set_gripper_value(g_open, 70)
        time.sleep(slow_s)
    
    goto_Home(mc)
    mc.send_coords(hover, move_fast)
    time.sleep(slow_s)
    mc.send_coords(pick, move_slow)
    time.sleep(slow_s)
    mc.set_gripper_value(g_closed, 70)
    time.sleep(slow_s)
    mc.set_gripper_value(g_closed, 70)
    time.sleep(slow_s)
    mc.send_coords(hover, move_slow)
    time.sleep(slow_s)

def goto_Grab_FK(mc, pick, hover):
    mc.set_gripper_value(g_open, 70)
    time.sleep(slow_s)
    
    goto_Home(mc)

    mc.set_gripper_value(g_open, 70)
    time.sleep(slow_s)
    mc.send_angles(hover, move_fast)
    time.sleep(slow_s)
    mc.send_angles(pick, move_slow)
    time.sleep(slow_s)
    mc.set_gripper_value(g_closed, 70)
    time.sleep(slow_s)
    mc.set_gripper_value(g_closed, 70)
    time.sleep(slow_s)
    mc.send_angles(hover, move_slow)
    time.sleep(slow_s)

def goto_Build(mc, pick, hover):
    goto_Home(mc)

    mc.send_coords(hover, move_fast)
    time.sleep(slow_s)
    mc.send_coords(pick, move_slow)
    time.sleep(slow_s)
    while mc.get_gripper_value() < 95:
        mc.set_gripper_value(g_open, 70)
        time.sleep(slow_s)
    mc.send_coords(hover, move_slow)
    time.sleep(slow_s)
    
    goto_Home(mc)


def goto_Build_FK(mc, pick, hover):
    goto_Home(mc)

    mc.send_angles(hover, move_fast)
    time.sleep(slow_s + 1)
    mc.send_angles(pick, move_slow)
    time.sleep(slow_s)
    while mc.get_gripper_value() < 95:
        mc.set_gripper_value(g_open, 70)
        time.sleep(slow_s)
    mc.send_angles(hover, move_slow)
    time.sleep(slow_s)

    goto_Home(mc)


goto_Grab_FK(mc3, [-22.32, 55.0, -95.53, -0.72, -52.11, 17.76], [-25.5, 61.03, -125.72, -5.18, -24.34, 27.33])
goto_Build(mc3, [211.2, 32.7, 61.1, 7.8, 83.97, 6.22], [203.6, 30.3, 98.0, 18.12, 76.09, 16.21])

goto_Grab_FK(mc6, [12.11, 36.38, -34.8, 6.5, -94.28, -17.86], [14.25, 23.16, -33.13, 4.83, -83.47, -16.45])
goto_Build(mc6, [185.9, -82.2, 68.6, 24.43, 80.12, 13.02], [201.4, -80.6, 110.0, 82.02, 85.64, 74.22])

goto_Grab_FK(mc3, [-21.79, 24.8, -16.17, -1.93, -88.33, 15.31], [-24.87, 9.58, -1.23, -4.04, -89.36, 20.19])
goto_Build(mc3, [215.2, 24.3, 142.2, 70.99, 83.4, 67.31], [215.8, 27.8, 161.6, 34.53, 85.32, 33.74])

goto_Grab_FK(mc6, [14.64, 44.72, -77.34, -32.16, 33.75, 34.48], [14.46, 44.93, -88.41, -31.2, 35.15, 33.22])
goto_Build(mc6, [183.1, -81.9, 154.8, 27.01, 78.75, 20.85],[196.1, -80.3, 184.0, 53.26, 81.3, 49.47])

goto_Grab(mc3, [197.8, -49.0, 232.2, -43.76, 89.07, -47.56], [174.3, -60.1, 256.4, 3.0, 72.81, -1.5])
goto_Build(mc3, [217.6, 29.8, 190.7, 171.13, 86.75, 173.24], [200.9, 33.5, 228.2, -21.17, 84.76, -18.49])

goto_Grab_FK(mc6, [17.31, 30.39, -13.53, -133.85, 35.94, 142.53], [16.69, 29.95, -31.37, -95.62, 24.34, 101.35])
goto_Build_FK(mc6, [-26.71, 29.26, -33.13, 92.19, 21.26, -86.74], [-29.79, 33.31, -62.75, 59.85, 35.33, -48.51])

goto_Grab_FK(mc3, [-19.59, 42.91, -31.81, -62.57, -11.86, 61.08], [-21.35, 33.91, -26.45, -53.7, -17.92, 52.64])
goto_Build_FK(mc3, [10.01, 29.2, -z6.67, 4.13, -97.29, -8.38], [12.12, 3.42, 13.18, 6.06, -89.63, -7.64])

goto_Grab_FK(mc6, [15.46, 59.67, -15.82, 40.16, -48.42, -21.03], [15.55, 45.48, -14.06, 41.13, -41.22, -29.15])
goto_Build(mc6, [143.2, -70.5, 234.1, 5.41, 6.73, -5.37], [79.8, -74.0, 266.7, 6.96, 5.64, -6.39])

goto_Grab(mc3, [213.4, -67.2, 92.4, 15.58, 88.34, 7.6], [213.4, -69.2, 150.4, 15.58, 88.34, 7.6])
goto_Build_FK(mc3, [11.45, 38.69, -48.69, 3.53, -81.73, -10.04], [13.52, -1.86, -6.85, 2.19, -79.27, -12.39])

goto_Grab_FK(mc6, [13.71, 89.8, -35.25, 32.16, -51.0, -12.04], [17.17, 65.67, -11.42, 33.31, -58.0, -17.82])
goto_Build(mc6, [125.4, -69.7, 301.3, 5.59, 3.64, -0.73], [79.5, -69.5, 330.2, 4.85, 8.63, 0.27])

# goto_Home(mc3)
# goto_Home(mc6)