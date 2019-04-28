'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given an array of numbers and an index i, return the index of the nearest larger number of the number at index i, where distance is measured in array indices.

For example, given [4, 1, 3, 5, 6] and index 0, you should return 3.

If two distances to larger numbers are the equal, then return any one of them. If the array at i doesn't have a nearest larger integer, then return null.

Follow-up: If you can preprocess the array, can you do this in constant time?
'''

array=[4,1,3,5,6,4]
index=0

def closest_larger_number(array,index):
    val = array[index]
    
    i=index
    j=index
    lenn=len(array)
    distance = 0
    while (i>0 or j<lenn-1):
        distance+=1
        if i>0:
            i-=1
        if j<lenn-1:
            j+=1
        val1=array[i]
        val2=array[j]
        if val1>val:
            return distance,i
        elif val2>val:
            return distance,j
    print('no larger number')
    return None
        

def closest_larger_number_with_preprocess(array,index):
    val=array[index]
    import numpy as np
    a=np.argsort(array)
    b=np.where(a==index)
    index_pos=b[0][0]
    while index_pos<len(array)-1:
        index_pos+=1
        if array[a[index_pos]]>val:
            return a[index_pos]

    print('no larger number')
    return None