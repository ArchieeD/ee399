import numpy as np 
from sympy import symbols, cos,sin,pi, simplify
from sympy.matrices import Matrix

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
# def get_transformation_matrix(a, alpha, d, theta):
#     M = Matrix([[cos(theta),            -sin(theta)*cos(alpha),            sin(theta)*sin(alpha),             a*cos(theta)         ],
#                 [sin(theta), cos(theta)*cos(alpha), -cos(theta) * sin(alpha), sin(theta)*a],
#                 [0, sin(alpha), cos(alpha),  d ],
#                 [0,                     0,                      0,            1          ]])
#     return M

overall_trans_matrix = Matrix(get_transformation_matrix(DH[0][0],DH[0][1], DH[0][2], DH[0][3] ))
for i in range(1, len(DH)):
    overall_trans_matrix = overall_trans_matrix * get_transformation_matrix(DH[i][0], DH[i][1], DH[i][2], DH[i][3])

#provide the joint angles, change later
joint_angles = [np.radians(-5.09),np.radians(74.7),np.radians(-46.31), np.radians(-0.26), np.radians(39.02), np.radians(1.93)]


#Define the offset parameters,
offsets = [0,0,0,0,0,0]

#map the joint angles and offsets into the tranformation matrix
subs_dict = {q + offset: joint_angle for q, offset, joint_angle in zip([q1, q2, q3, q4, q5, q6], offsets, joint_angles)}
#print(subs_dict)
#end effector position
x = simplify(overall_trans_matrix[0,3])
y = simplify(overall_trans_matrix[1,3])
z = simplify(overall_trans_matrix[2,3])

sub_x = x.subs(subs_dict)
sub_y = y.subs(subs_dict)
sub_z = z.subs(subs_dict)
print(sub_x)
print(sub_y)
print(sub_z)
