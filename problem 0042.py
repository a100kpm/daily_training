'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given a list of integers S and a target number k, write a function that returns
 a subset of S that adds up to k. If such a subset cannot be made, then return null.

Integers can appear more than once in the list. You may assume all numbers in 
the list are positive.

For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] 
since it sums up to 24.
'''

S = [12, 1 ,61 ,5 ,9 ,2]

k=24

def bon_compte(S,k):
    lenn=len(S)
    tentative_max=2**lenn
    List=[]
    
    for i in range(tentative_max):
        j=nbr_to_bi(i,lenn)
        compte=0
        for kkk in range(lenn):
            compte+=S[kkk]*j[kkk]
        if compte==k:
            for kk in range(lenn):
                if j[kk]==1:
                    List.append(S[kk])
            return List
    return None
        
        
        
        
def nbr_to_bi(i,lenn):
    result=[]
    for _ in range(lenn):
        result.append(0)
    for j in range(lenn):
        if i%2==1:
            result[j]=1
            i=i-1
        i=i/2
    return result