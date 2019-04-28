'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Goldman Sachs.

You are given N identical eggs and access to a building with k floors. Your task 
is to find the lowest floor that will cause an egg to break, if dropped from that floor. 
Once an egg breaks, it cannot be dropped again. If an egg breaks when dropped from the xth floor, 
you can assume it will also break when dropped from any floor greater than x.

Write an algorithm that finds the minimum number of trial drops it will take, in the worst case, to identify this floor.

For example, if N = 1 and k = 5, we will need to try dropping the egg at every floor, 
beginning with the first, until we reach the fifth floor, so our solution will be 5.
'''
import math


def find_lowest_attempt(n,k):
    if k==0:
        return 0
    if k==1:
        return 1
    if n==1:
        return k
    if n==2:
        compteur=0
        i=0
        while compteur<k:
            i+=1
            compteur+=i

        return i
    
    val=[]
    for i in range(1,k):
        a=find_lowest_attempt(n-1,i-1)
        b=find_lowest_attempt(n,k-i)
        val.append(1+max(a,b))
        
    return min(val)
    