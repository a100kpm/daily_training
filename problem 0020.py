'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given two singly linked lists that intersect at some point, 
find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
'''

A=[3,7,8,10]
B=[99,1,8,10]


def find_link(List1,List2):
    lenn=len(A)
    lenn2=len(B)
    
    i=0
    j=0
    
    while j<lenn2:
        if A[i]==B[j]:
            return A[i]
        i+=1
        if i==lenn:
            i=0
            j+=1
    print('no link')
    return None
            
        
        
    