'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.

For example, given the following matrix:

[[1,  2,  3,  4,  5],
 [6,  7,  8,  9,  10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]]

You should print out the following:

1
2
3
4
5
10
15
20
19
18
17
16
11
6
7
8
9
14
13
12
'''
import numpy as np


matrice = np.array([[1,  2,  3,  4,  5],
 [6,  7,  8,  9,  10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]])

def asticot_printer(matrix):
    base1=0
    base2=1
    coorX=0
    coorY=0
    base1_max=np.shape(matrix)[1]-1
    base2_max=np.shape(matrix)[0]-1
    
    taille_=np.shape(matrix)[0]*np.shape(matrix)[1]-1
    direction=0
    for _ in range(taille_):
        print(matrix[coorY][coorX])
        if direction==0:
            coorX+=1
            if coorX==base1_max:
                direction=1
                base1_max-=1
        elif direction==1:
            coorY+=1
            if coorY==base2_max:
                direction=2
                base2_max-=1
        elif direction==2:
            coorX-=1
            if coorX==base1:
                direction=3
                base1+=1
        else:
            coorY-=1
            if coorY==base2:
                direction=0
                base2+=1
                
    print(matrix[coorY][coorX])
        