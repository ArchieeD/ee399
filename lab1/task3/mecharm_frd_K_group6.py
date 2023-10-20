import numpy as np 
from sympy import symbols, cos,sin,pi, simplify
from sympy.matrices import Matrix
import sys
sys.path.insert(0,'/Users/archiedeng/Documents/ee399/lab1/task2') 
from extract_values import read_csv


neutral_start_pos = [0,0,0,0,0,0]

q1, q2, q3, q4, q5, q6 = symbols('q1 q2 q3 q4 q5 q6')

DH=[[0,   0,        114,  q1],
    [0,   -pi/2,    0,    q2-(pi/2)],
    [100, 0,        0,    q3],
    [10,  -pi/2,    96,   q4],
    [0,   pi/2,     0,    q5],
    [0,   -pi/2,    56.5, q6]]


def get_transformation_matrix(a, alpha, d, theta):
    M = Matrix([[cos(theta),            -sin(theta),            0,             a         ],
                [sin(theta)*cos(alpha), cos(theta)*cos(alpha), -sin(alpha), -sin(alpha)*d],
                [sin(theta)*sin(alpha), cos(theta)*sin(alpha), cos(alpha),  cos(alpha)*d ],
                [0,                     0,                      0,            1          ]])
    return M

# Calculate overall transformation matrix
overall_trans_matrix = Matrix(get_transformation_matrix(DH[0][0],DH[0][1], DH[0][2], DH[0][3] ))
for i in range(1, len(DH)):
    overall_trans_matrix = overall_trans_matrix * get_transformation_matrix(DH[i][0], DH[i][1], DH[i][2], DH[i][3])


#Define the offset parameters,
offsets = [0,0,0,0,0,0]

#map the joint angles and offsets into the tranformation matrix
#end effector position
x = simplify(overall_trans_matrix[0,3])
y = simplify(overall_trans_matrix[1,3])
z = simplify(overall_trans_matrix[2,3])

joint_angles_list = read_csv('../task2/final_values.csv', 'a')
coords_list = read_csv('../task2/final_values.csv', 'c')

print("angle,",'x(calc),','y(calc),','z(calc),','x(meas),','y(meas),','z(meas),','x(error%),','y(error%),','z(error%)')
i = 0
for joint_angles in joint_angles_list:
    for j in range(len(joint_angles)): joint_angles[j] = np.radians(joint_angles[j])
    subs_dict = {q + offset: joint_angle for q, offset, joint_angle in zip([q1, q2, q3, q4, q5, q6], offsets, joint_angles)}
    sub_x = x.subs(subs_dict)
    sub_y = y.subs(subs_dict)
    sub_z = z.subs(subs_dict)
    calc_pos = [sub_x, sub_y, sub_z]
    print(np.round(np.degrees(joint_angles),2),',',np.round(np.array(calc_pos).astype(np.float),3).tolist(),','
          , coords_list[i][:3],',', 
          np.round(np.divide((np.abs(np.subtract(calc_pos,coords_list[i][:3])*100)), calc_pos).astype(np.float),3).tolist())
    i+=1