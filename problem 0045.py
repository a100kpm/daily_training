'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Two Sigma.

Using a function rand5() that returns an integer from 1 to 5 (inclusive)
 with uniform probability, implement a function rand7() that returns an integer 
 from 1 to 7 (inclusive).
'''

import random

#a=random.randrange(1,6)
#b=random.randrange(1,8)

a=[0]*8

    
def randomer7():
    a=1
    b=1
    while a ==1 and b<5:
        a=random.randrange(1,6)
        b=random.randrange(1,6)
    if a==1:
        return 1
    if a==2 and b<3:
        return 1
    elif a==2:
        return 2
    if a==3 and b<4:
        return 3
    elif a==3:
        return 4
    if a==4 and b==1:
        return 4
    if a==4 and b<5:
        return 5
    elif a==4:
        return 6
    if a==5 and b<3:
        return 6
    return 7
    
'''

512
345
123
451
234
512
345
'''


for _ in range(10000000):
    b=0
    b+=randomer7()
    a[b]+=1

print(a)