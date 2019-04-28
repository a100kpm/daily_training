'''
Good morning! Here's your coding interview problem for today.

This question was asked by Zillow.

You are given a 2-d matrix where each cell represents number of coins in that cell. 
Assuming we start at matrix[0][0], and can only move right or down, 
find the maximum number of coins you can collect by the bottom right corner.

For example, in this matrix

0 3 1 1
2 0 0 4
1 5 3 1

The most we can collect is 0 + 2 + 1 + 5 + 3 + 1 = 12 coins.
'''

import numpy as np

matrix = np.array([ [0, 3, 1, 1],
                    [2, 0, 0, 4],
                    [1, 5, 3, 1] 
                                ])

def gold_collector(matrix):
    lenn=np.shape(matrix)[0]
    lenn2=np.shape(matrix)[1]
    new_matrix=np.copy(matrix)
    for i in range(1,lenn2):
        new_matrix[0][i]=new_matrix[0][i]+new_matrix[0][i-1]
    for j in range(1,lenn):
        new_matrix[j][0]=new_matrix[j][0]+new_matrix[j-1][0]
    for j in range(1,lenn):
        for i in range(1,lenn2):
            new_matrix[j][i]=new_matrix[j][i]+max(new_matrix[j-1][i],new_matrix[j][i-1])
    return new_matrix[-1][-1]