'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

You are given an array of nonnegative integers. 
Let's say you start at the beginning of the array and are trying to advance to the end.
 You can advance at most, the number of steps that you're currently on. 
 Determine whether you can get to the end of the array.

For example, given the array [1, 3, 1, 2, 0, 1], we can go from indices 0 -> 1 -> 3 -> 5, so return true.

Given the array [1, 2, 1, 0, 0], we can't reach the end, so return false.
'''

array = [1,3,1,2,0,1]
array2= [1,2,1,0,0]

def can_jump(array):
    if len(array)<=1:
        return True
    
    lenn=len(array)-1
    
    for i in range(lenn):
        if i+array[i]>=lenn:
            a=can_jump(array[:i+1])
            if a==True:
                return True
            
    return False