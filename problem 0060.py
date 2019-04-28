'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given a multiset of integers, return whether it can be partitioned into two 
subsets whose sums are the same.

For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, it would return true, 
since we can split it up into {15, 5, 10, 15, 10} and {20, 35}, which both add up to 55.

Given the multiset {15, 5, 20, 10, 35}, it would return false, 
since we can't split it up into two subsets that add up to the same sum.
'''

List = [15,5,20,10,35,15,10]

def splitage(List):
    if sum(List)%2==1:
        return False
    n=len(List)-1
    return finder(List,sum(List)/2,n)

def finder(List,dem_sum,n):
    if dem_sum==0:
        return True
    if n==0:
        return False
    return finder(List,dem_sum-List[n],n-1) or finder(List,dem_sum,n-1)
        