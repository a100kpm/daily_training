'''
Good morning! Here's your coding interview problem for today.

This question was asked by Google.

Given an integer n and a list of integers l, write a function that randomly 
generates a number from 0 to n-1 that isn't in l (uniform).
'''


List = [5,4,13,12,11]

import random

def random_bar(n,List):
    i=List[0]
    
    while i in List:
        i=random.randrange(1,n)
        
    return i


n=15

test=[0]*(n+1)

for i in range(1000000):
    j=random_bar(n,List)
    test[j]+=1