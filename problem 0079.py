'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given an array of integers, write a function to determine whether 
the array could become non-decreasing by modifying at most 1 element.

For example, given the array [10, 5, 7], you should return true, 
since we can modify the 10 into a 1 to make the array non-decreasing.

Given the array [10, 5, 1], you should return false, 
since we can't modify any one element to get a non-decreasing array.
'''

List = [10,5,7]
List2 = [10,5,1]
List3 = [10,2,3,4,5,1]

def dodge_decrease(List):
    lenn=len(List)
    if lenn<=2:
        return True
    compteur=0
    a=List[0]
    b=List[1]
    i=2
    if b<a:
        compteur+=1
        a=b
    while compteur<2:
        c=List[i]
        if c<b:
            compteur+=1
            c=b
        b=c
        i+=1
        if i==lenn:
            break
    if compteur<=1:
        return True
    return False