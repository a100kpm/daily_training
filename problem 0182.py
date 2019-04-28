'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

A graph is minimally-connected if it is connected and there is no edge that 
can be removed while still leaving the graph connected. For example, 
any binary tree is minimally-connected.

Given an undirected graph, check if the graph is minimally-connected.
 You can choose to represent the graph as either an adjacency matrix or adjacency list.
'''

#            0
#           / \
#          1   2
#         / \   \
#        3   4   5  
        

import numpy as np

matrix = np.array([
        [0,1,1,0,0,0],
        [1,0,0,1,1,0],
        [1,0,0,0,0,1],
        [0,1,0,0,0,0],
        [0,1,0,0,0,0],
        [0,0,1,0,0,0],
                ])

def is_minimal(matrix_):
    matrix=matrix_.copy()
    lenn=np.shape(matrix)[0]
    pos_start=-1
    for i in range(lenn):
        compteur=0
        for j in range(lenn):
            if matrix[i,j]==1:
                compteur+=1
        if compteur==1:
            pos_start=i
            break
        
    if pos_start==-1:
        return False
    
    List=[pos_start]
    List_reached=[pos_start]

    next_=True
    while next_:
        pos=List[0]
        List=List[1:]
        
        for i in range(lenn):
            if matrix[pos,i]==1:
                matrix[i][pos]=0
                List.append(i)
                if i in List_reached:
                    return False
                else:
                    List_reached.append(i)
                
        if len(List)==0:
            next_=False
            
    return True
            
        