'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

Given an array of numbers, find the length of the longest increasing subsequence in the array. 
The subsequence does not necessarily have to be contiguous.

For example, given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], 
the longest increasing subsequence has length 6: it is 0, 2, 6, 9, 11, 15.
'''

List=[0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]


def find_longest(List):
    lenn=len(List)
    new_List=[0]*lenn
    
    for i in range(lenn-1,-1,-1):
        new_List[i]=score(i,List,new_List,lenn)
    
    val=max(new_List)
    
    return val

def score(i,List,new_List,lenn):
    choice=[]
    for j in range(i+1,lenn):
        if List[i]<List[j]:
            choice.append(new_List[j])
    if choice==[]:
        return 1
    return (max(choice)+1)
    
    
    