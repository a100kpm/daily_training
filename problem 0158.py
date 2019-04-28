'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Slack.

You are given an N by M matrix of 0s and 1s. Starting from the top left corner, how many ways are there to reach the bottom right corner?

You can only move right and down. 0 represents an empty space while 1 represents a wall you cannot walk through.

For example, given the following matrix:

[[0, 0, 1],
 [0, 0, 1],
 [1, 0, 0]]

Return two, as there are only two ways to get to the bottom right:

    Right, down, down, right
    Down, right, down, right

The top left corner and bottom right corner will always be 0.
'''

import numpy as np

matrice = np.array([[0, 0, 1],
                     [0, 0, 1],
                     [1, 0, 0]])
    

def number_path(matrice,pos=[0,0]):

    N,M=np.shape(matrice)
    if pos==[N-1,M-1]:
        return 1
    
    if matrice[pos[0],pos[1]]==1:
        return 0
    
    a=0
    b=0
    if pos[0]<N-1:
        a=number_path(matrice,[pos[0]+1,pos[1]])
    if pos[1]<M-1:
        b=number_path(matrice,[pos[0],pos[1]+1])
        
    return a+b
    