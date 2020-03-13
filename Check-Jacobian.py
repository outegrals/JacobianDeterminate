from sympy import *
import math
import sys
import random

def main():
    input = sys.argv[1]
    f = open(input, 'r')
    file = f.readlines()
    thetaInput = []
    for line in file:
        x = line.rstrip('\n')
        x = x.split(',')
        x = [int(i) for i in x]
        thetaInput.append(x)
    f.close()

    output = []

    for x in thetaInput:
        #setting theta values as radians
        theta1 = math.radians(x[0])
        theta2 = math.radians(x[1])
        theta3 = math.radians(x[2])
        theta4 = math.radians(x[3])
        theta5 = math.radians(x[4])
        theta6 = math.radians(x[5])
        #DH parameter matrix
        H1 = Matrix([[math.cos(theta1), 0, math.sin(theta1), 0], 
                            [math.sin(theta1), 0, -math.cos(theta1), 0], 
                            [0, 1, 0, .1625],
                            [0,0,0,1]])
        H2 = Matrix([[math.cos(theta2), -math.sin(theta2), 0, -.425*math.cos(theta2)],
                            [math.sin(theta2), math.cos(theta2), 0, -.425*math.sin(theta2)],
                            [0,0,1,0],
                            [0,0,0,1]])
        H3 = Matrix([[math.cos(theta3), -math.sin(theta3), 0, -.3922*math.cos(theta3)],
                            [math.sin(theta3), math.cos(theta3), 0, -.3922*math.sin(theta3)],
                            [0,0,1,0],
                            [0,0,0,1]])
        H4 = Matrix([[math.cos(theta4), 0, math.sin(theta4), 0], 
                            [math.sin(theta4), 0, -math.cos(theta4), 0], 
                            [0, 1, 0, .1333],
                            [0,0,0,1]])
        H5 = Matrix([[math.cos(theta5), 0, -math.sin(theta5), 0], 
                            [math.sin(theta5), 0, math.cos(theta5), 0], 
                            [0, -1, 0, .0997],
                            [0,0,0,1]])
        H6 = Matrix([[math.cos(theta6), -math.sin(theta6), 0,0],
                            [math.sin(theta6), math.cos(theta6), 0, 0],
                            [0,0,1,.0996],
                            [0,0,0,1]])
        #Forward kinematics
        T0_to_1 = H1
        T0_to_2 = T0_to_1*H2
        T0_to_3 = T0_to_2*H3
        T0_to_4 = T0_to_3*H4
        T0_to_5 = T0_to_4*H5
        T0_to_6 = T0_to_5*H6

        #finding position matrix
        O6 = Matrix(T0_to_6.col(-1)[0:3])
        O5 = Matrix(T0_to_5.col(-1)[0:3])
        O4 = Matrix(T0_to_4.col(-1)[0:3])
        O3 = Matrix(T0_to_3.col(-1)[0:3])
        O2 = Matrix(T0_to_2.col(-1)[0:3])
        O1 = Matrix(H1.col(-1)[0:3])

        #finding z axis matrix
        z0 = Matrix([[0], [0], [1]])
        z1 = Matrix(T0_to_1.col(2)[0:3])
        z2 = Matrix(T0_to_2.col(2)[0:3])
        z3 = Matrix(T0_to_3.col(2)[0:3])
        z4 = Matrix(T0_to_4.col(2)[0:3])
        z5 = Matrix(T0_to_5.col(2)[0:3])
        
        #finding linear velocity
        v1 = z0.cross(O6)
        v2 = z1.cross(O6 - O1)
        v3 = z2.cross(O6 - O2)
        v4 = z3.cross(O6 - O3)
        v5 = z4.cross(O6 - O4)
        v6 = z5.cross(O6 - O5)
        #making it as one big matrix 
        VJ = v1.col_insert(1, v2)
        VJ = VJ.col_insert(2, v3)
        VJ = VJ.col_insert(3, v4)
        VJ = VJ.col_insert(4, v5)
        VJ = VJ.col_insert(5, v6)
        #finding angular velocity, basically the Z into a big matrix
        WJ = z0.col_insert(1, z1)
        WJ = WJ.col_insert(2, z2)
        WJ = WJ.col_insert(3, z3)
        WJ = WJ.col_insert(4, z4)
        WJ = WJ.col_insert(5, z5)
        #combine the two
        J = VJ
        J = J.row_insert(3, WJ)
        #find det and save into list
        print(J.det())
        if J.det() < 0.001:
            output.append(1)
        else:
            output.append(0)
    #Go through list and output to file 1 or 0 if small or not
    f = open('output.txt', 'w')
    for x in output:
        f.write('%d\n' %(x))
    f.close()
    print('Results have been saved into Output.txt')
main()