'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given an array of numbers of length N, find both the minimum and maximum using less than 2 * (N - 2) comparisons.
'''


import random
import math
# =============================================================================
# =============================================================================
# # ou bien tout simplement check si c'est plus petit que le min, et sinon seulement 
# # check si c'est plus grand que le max
# =============================================================================
# =============================================================================

array = [19, 31, 8, 32, 6, 0, 39, 31, 32, 12]

#si 10 --> inférieur a 18

def find_min_max(List):
    array=List.copy()
    lenn=len(array)
    comparaison=0
    
    for i in range(math.floor(lenn/2)):
        comparaison+=1
        if array[2*i]<array[2*i+1]:
            a=array[2*i]
            array[2*i]=array[2*i+1]
            array[2*i+1]=a
            
    min_=array[0]
    max_=array[1]
    
    for i in range(math.floor(lenn/2)):
        comparaison+=1
        if min_>array[2*i]:
            min_=array[2*i]
        comparaison+=1
        if max_<array[2*i+1]:
            max_=array[2*i+1]
            
    print(comparaison)
#    il peut y avoir jusqu'a 2 comparaison en plus
    if array[-1]<min_:
        min_=array[-1]
    elif array[-1]>max_:
        max_=array[-1]
        
    
    return min_,max_
    
    
    