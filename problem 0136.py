'''
Good morning! Here's your coding interview problem for today.

This question was asked by Google.

Given an N by M matrix consisting only of 1's and 0's, find the largest 
rectangle containing only 1's and return its area.

For example, given the following matrix:

[[1, 0, 0, 0],
 [1, 0, 1, 1],
 [1, 0, 1, 1],
 [0, 1, 0, 0]]

Return 4.
'''

import numpy as np

matrix = np.array([[1, 0, 0, 0],
                   [1, 0, 1, 1],
                   [1, 0, 1, 1],
                   [0, 1, 0, 0]])

def max_rectangle(matrix):
    lenn=np.shape(matrix)[0]
    lenn2=np.shape(matrix)[1]
    taille_max=0
    for i in range(lenn):
        for j in range(lenn2):
            if matrix[i][j]==1:
                taille=find_taille(i,j,lenn,lenn2,matrix)
                if taille>taille_max:
                    taille_max=taille
    return taille_max

def find_taille(i,j,lenn,lenn2,matrix):
    largeur=0
    for k in range(j,lenn2):
        if matrix[i][k]==1:
            largeur+=1
        else:
            break
        
    taille_m=0
    taille=0
    for k in range(largeur):
        k1=i
        next_=True
        taille=k+1
        while next_==True and k1<lenn-1:
            k1+=1
            for k2 in range(k+1):
                if matrix[k1][j+k2]==0:
                    next_==False
                    taille-=(k+1)
                    break
            taille+=(k+1)
                
        
#        print(taille)
        if taille_m<taille:
            taille_m=taille
        taille=0
        
    return taille_m