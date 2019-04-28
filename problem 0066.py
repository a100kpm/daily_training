'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Square.

Assume you have access to a function toss_biased() which returns 0 or 1 with a 
probability that's not 50-50 (but also not 0-100 or 100-0). 
You do not know the bias of the coin.

Write a function to simulate an unbiased coin toss.
'''

import random

screw = random.randrange(1,100)


def toss_biased(screw=screw):
    if random.randrange(0,101)<screw:
        return 0
    return 1


def try_random(screw=screw):
    score = 0
    for _ in range(100):
        score+= toss_biased(screw)
    
    
    restart=True
        
    while restart:
        test = 0
        
        for _ in range(100):
            test += toss_biased(screw)
            
        if test!=score:
            restart=False
    
    if test<score:
        return 0
    return 1
        
print(screw) 
val=[]
for _ in range(100):
    aaa=0
    for _ in range(10000):
        aaa+=try_random()
    val.append(aaa)
    
