'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given a list of integers, return the largest product that can be made by multiplying any three integers.

For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.

You can assume the list has at least three integers.
'''

import numpy as np

List = [-10,-10,5,2]

def max_multi(List):
    nega = []
    score = 1
    lenn=len(List)
    
    for i in range(lenn):
        if List[i]>0:
            score=score*List[i]
        elif List[i]<0:
            nega.append(List[i])
    
    lenn2=len(nega)
    avoid=1
    if lenn2%2==1:
        avoid = max(nega)
    for i in range(lenn2):
        score=score*nega[i]
    score=score*avoid
    
    return score

def max_3_multy(List):
    nega=[0,0,0]
    posi=[0,0,0]
    lenn=len(List)
    
    for i in range(lenn):
        if List[i]>0:
            posi.append(List[i])
        else:
            nega.append(List[i])
    
    top1=max(posi)
    posi[np.argmax(posi)]=0
    top2=max(posi)
    posi[np.argmax(posi)]=0
    top3=max(posi)
    
    bot1=min(nega)
    nega[np.argmin(nega)]=0
    bot2=min(nega)
    
    nega_val = bot1*bot2
    posi_val = top2*top3
    
    if nega_val>posi_val:
        return top1*nega_val
    return top1*posi_val