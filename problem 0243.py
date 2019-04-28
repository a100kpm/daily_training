'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Etsy.

Given an array of numbers N and an integer k, your task is to split N 
into k partitions such that the maximum sum of any partition is minimized. Return this sum.

For example, given N = [5, 1, 2, 7, 3, 4] and k = 3, you should return 8, 
since the optimal partition is [5, 1, 2], [7], [3, 4].
'''

N = [5, 1, 2, 7, 3, 4] 
k = 3

def opti_sum(N,k):
    List=[0]*k
    
    return opti(N,List,k)


def opti(N,List,k):
    
    if len(N)==0:
        return max(List)
    
    val=[0]*k
    
    for i in range(k):
        List[i]+=N[0]
        val[i]=opti(N[1:],List,k)
        List[i]-=N[0]
    
    return min(val)