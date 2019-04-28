'''Good morning! Here's your coding interview problem for today.

This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
'''

import time
import random

a = random.randint(100,110)
List = []
for i in range(a):
    List += [random.randint(-10,10)]
    
    
#Si all >0
def max_sum(List):
    if len(List)==0:
        return 0
    elif List[0]<=0:
        return max_sum(List[1:])
    if len(List)==1:
        return List[0]
    if len(List)==2:
        return max(List[0],List[1])
    else:
        return max(List[0]+max_sum(List[2:]),List[1]+max_sum(List[3:]))
    

def bonus_max_sum(List):
    lenn=len(List)
    for n in range(lenn):
        if List[n]<0:
            List[n]=0
    if lenn==0:
        return 0
    if lenn==1:
        return List[0]
    if lenn==2:
        return max(List[0],List[1])
    else:
        List[2]+=List[0]
        for n in range(3,lenn):
            List[n]+=max(List[n-2],List[n-3])
        return max(List[-1],List[-2])
    
print(List)
start_time = time.clock()
print(max_sum(List))
print(time.clock() - start_time, "seconds")
print(bonus_max_sum(List))
print(time.clock() - start_time, "seconds")
        
    
        