'''
Good morning! Here's your coding interview problem for today.

This problem was asked by MongoDB.

Given a list of elements, find the majority element,
 which appears more than half the time (> floor(len(lst) / 2.0)).

You can assume that such element exists.

For example, given [1, 2, 1, 1, 3, 4, 0], return 1.
'''
import math
List = [1,2,1,1,3,4,0]

def find_majority(List):
    lenn=len(List)
    threshold = math.floor(lenn/2.0)
    dictt=dict()
    for i in range(lenn):
        if List[i] not in dictt:
            dictt[List[i]]=0

        dictt[List[i]]+=1
        if dictt[List[i]]>=threshold:
            return List[i]