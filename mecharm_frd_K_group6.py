import numpy as np 
from sympy import symbols, cos,sin,pi, simplify
from sympy.matracis import Matrix

neutral_start_pos = [0,0,0,0,0,0]

q1, q2, q3, q4, q5, q6 = symbols('q1 q2 q3 q4 q5 q6')

DH=[[0,     -pi/2,   100,  q1],
    [100,   0,       0,    q2+(pi/2)],
    [10,    -pi/2,   0,    q3],
    [0,     pi/2,    50,   q4],
    [0,     -pi/2,   0,    q5],
    [0,     0,       55, q6]]

def get_transformation_matrix(a, alpha, d, theta):
    M = Matrix([[cos(theta),            -sin(theta),            0,             a         ],
                [sin(theta)*cos(alpha), cos(theta)*cos(alpha), -sin(alpha), -sin(alpha)*d],
                [sin(theta)*sin(alpha), cos(theta)*sin(alpha), cos(alpha),  cos(alpha)*d ],
                [0,                     0,                      0,            1          ]])
    return M

overall_trans_matrix = get_transformation_matrix(DH[0][0], DH[0][1], DH[0][2], DH[0][3])*
                       get_transformation_matrix(DH[1][0], DH[1][1], DH[1][2], DH[1][3])*
                       get_transformation_matrix(DH[2][0], DH[2][1], DH[2][2], DH[2][3])*
                       get_transformation_matrix(DH[3][0], DH[3][1], DH[3][2], DH[3][3])*
                       get_transformation_matrix(DH[4][0], DH[4][1], DH[4][2], DH[4][3])*
                       get_transformation_matrix(DH[5][0], DH[5][1], DH[5][2], DH[5][3])

#provide the joint angles, change later
joint_angles = [np.radians(45), np.radians(45), np.radians(45), 
                np.radians(45), np.radians(45), np.radians(45)]

#Define the offset parameters,
offsets = [0,0,0,0,0,0]

#map the joint angles and offsets into the tranformation matrix
#subs_dict = {q + offset: angles for q, offset, angle in zip([q1, q2, q3, q4, q5, q6], offsets, joint_angles)}

#end effector position
x = simplify(overall_trans_matrix[0,3])
y = simplify(overall_trans_matrix[1,3])
z = simplify(overall_trans_matrix[2,3])
