'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Apple.

A fixed point in an array is an element whose value is equal to its index. 
Given a sorted array of distinct elements, return a fixed point, if one exists. Otherwise, return False.

For example, given [-6, 0, 2, 40], you should return 2. Given [1, 5, 7, 8], you should return False.
'''


List1=[-6,0,2,40]
List2=[1,5,7,8]


def find_fixed_point(List):
    lenn=len(List)
    for i in range(lenn):
        if i==List[i]:
            return i
    return False