'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given an array of elements, return the length of the longest subarray where all its elements are distinct.

For example, given the array [5, 1, 3, 5, 2, 3, 4, 1], return 5 as the longest subarray of distinct elements is [5, 2, 3, 4, 1].
'''


array=[5, 1, 3, 5, 2, 3, 4, 1]

def longest_unique_subarray(array):
    lenn=len(array)
    result=0
    i=0
    
    score=0
    dictio=set()
    for i in range(lenn):
        if array[i] not in dictio:
            dictio.add(array[i])
            score+=1
        else:
            result=max(result,score)
            score=1
            dictio=set()
            dictio.add(array[i])
            
    return max(score,result)
            
