'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

A builder is looking to build a row of N houses that can be of K different colors.
 He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

Given an N by K matrix where the nth row and kth column represents the cost to build
 the nth house with kth color, return the minimum cost which achieves this goal.
'''

import random
import numpy as np


N=10
K=4
valeurs=random.randrange(K+1,10)

Cost_mat=np.zeros([K,N])
for i in range(K):
    for j in range(N):
        Cost_mat[i,j]=random.randrange(1,valeurs)
        

def min_cost(Cost_mat):
    lenn=np.shape(Cost_mat)[1]
    lenn2=np.shape(Cost_mat)[0]
    
    for i in range(1,lenn):
        current_choix=Cost_mat[:,i-1].tolist()
        for j in range(lenn2):
            current_choix_local=current_choix[:j]+current_choix[j+1:]
            Cost_mat[j,i]+=min(current_choix_local)
            
            
    return min(Cost_mat[:,lenn-1])
  
        
        
print(Cost_mat)
print('-------')
print(min_cost(Cost_mat))
            
            
            
            
            
            
    
    
    
    
    
    
    
        
