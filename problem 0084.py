'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Given a matrix of 1s and 0s, return the number of "islands" in the matrix. 
A 1 represents land and 0 represents water, so an island is a group of 1s that are neighboring and their perimiter is surrounded by water.

For example, this matrix has 4 islands.

1 0 0 0 0
0 0 1 1 0
0 1 1 0 0
0 0 0 0 0
1 1 0 0 1
1 1 0 0 1
'''

import numpy as np

islands = np.array([[1 ,0 ,0 ,0 ,0],[0 ,0 ,1 ,1 ,0],[0, 1, 1, 0, 0],[0, 0, 0, 0, 0],[1 ,1 ,0 ,0 ,1],[1 ,1 ,0 ,0 ,1]])


def nbr_islands(islands):
    checked = islands*0
    
    lenn=np.shape(islands)[0]
    lenn2=np.shape(islands)[1]
    val=3
    
    for i in range(lenn):
        for j in range(lenn2):
            if checked[i][j]==0:
                checked[i][j]=1
                if islands[i][j]==1:
                    search_link(islands,i,j,checked,val,lenn,lenn2)
                    val+=1


    print(islands)
    print('')
    print(checked)
    return val-3

def search_link(islands,i,j,checked,val,lenn,lenn2):
    checked[i][j]=1
    islands[i][j]=val
    if i>0:
        if checked[i-1][j]==0 and islands[i-1][j]==1:
            search_link(islands,i-1,j,checked,val,lenn,lenn2)
        else:
            checked[i-1][j]=1
    if i<lenn-1:
        if checked[i+1][j]==0 and islands[i+1][j]==1:
            search_link(islands,i+1,j,checked,val,lenn,lenn2)
        else:
            checked[i+1][j]=1
    if j>0:
        if checked[i][j-1]==0 and islands[i][j-1]==1:
            search_link(islands,i,j-1,checked,val,lenn,lenn2)
        else:
            checked[i][j-1]=1
    if j<lenn2-1:
        if checked[i][j+1]==0 and islands[i][j+1]==1:
            search_link(islands,i,j+1,checked,val,lenn,lenn2)
        else:
            checked[i][j+1]=1
    
            