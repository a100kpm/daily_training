'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Given an array and a number k that's smaller than the length of the array, 
rotate the array to the right k elements in-place.
'''

import random


array=[]
for i in range(10):
    array.append(random.randrange(1,10))
   
    
def decal_array(array,k):
    lenn=len(array)
    if k>=lenn:
        print('k too big')
        return
    
    a=array[lenn-k:].copy()
    array[lenn-k:]
    
    result = array.copy()
    
    result[k:] = result[:lenn-k]
    result[:k]=a[:]
    
    return result