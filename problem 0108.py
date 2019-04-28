'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given two strings A and B, return whether or not A can be shifted some number of times to get B.

For example, if A is abcde and B is cdeab, return true. If A is abc and B is acb, return false.
'''


def can_shift(A,B):
    lenn=len(A)
    start=B[0]
    
    List_start=[]
    
    for i in range(lenn):
        if A[i]==start:
            List_start.append(i)
    
    lenn2=len(List_start)
    for i in range(lenn2):
        for j in range(lenn):
            val=(List_start[i]+j)%lenn
            
            if B[j]!=A[val]:
                break
            if j==lenn-1:
                return True
    return False