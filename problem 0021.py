'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Snapchat.

Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), 
find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
'''

import numpy as np

List=[[30,75],[0,50],[60,150],[30,60],[20,40],[70,130],[25,120]]

def min_room(List):
    lenn=len(List)
    start=List[0][0]
    end=List[0][1]
    for i in range(1,lenn):
        if List[i][0]<start:
            start=List[i][0]
        if List[i][1]>end:
            end=List[i][1]
    
    checkers=np.zeros(end-start)
    
    for i in range(lenn):
        adder=np.ones(List[i][1]-List[i][0])
#        lenn2=len(adder)
        checkers[List[i][0]-start:List[i][1]-start]+=adder
    return max(checkers)
    