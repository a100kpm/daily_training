'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Uber.

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand. 
Find the minimum element in O(log N) time. You may assume the array does not contain duplicates.

For example, given [5, 7, 10, 3, 4], return 3.
'''

import math

array = [5,7,10,3,4]
array2 = [6,7,10,3,4,5]

def find_pivot_number(array):
    lenn=len(array)
    
    start=0
    end=lenn-1
    middle=math.floor(end/2)
    
    while start!=end:
        val_start=array[start]
        val_middle=array[middle]
        val_end=array[end]
        
        if val_start>val_middle:
            print("cas1")
            end=middle
            middle=math.floor( (start+end)/2 )
            
        elif val_middle>val_end:
            if start==middle:
                return start
            print("cas2")
            start=middle
            middle=math.floor( (start+end)/2 )
            
        else:
            print("cas3")
            return start
        
        print('start=',start)
        print('middle=',middle)
        print('end=',end)
        input()
        
    return start