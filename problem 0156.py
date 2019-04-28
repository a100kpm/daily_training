'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given a positive integer n, find the smallest number of squared integers which sum to n.

For example, given n = 13, return 2 since 13 = 3*2 + 2*2 = 9 + 4.

Given n = 27, return 3 since 27 = 3**2 + 3**2 + 3**2 = 9 + 9 + 9.
'''

#32  -> 16 16
#32  -> 25 4 1 1 1

import math

def get_min_square(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    max_test=math.floor(math.sqrt(num))+1
    List=[]
    for i in range(1,max_test):
        List.append(1+get_min_square(num-i**2))
    return min(List)

