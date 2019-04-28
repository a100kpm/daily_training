'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given a set of closed intervals, find the smallest set of numbers 
that covers all the intervals. If there are multiple smallest sets, return any of them.

For example, given the intervals [0, 3], [2, 6], [3, 4], [6, 9], 
one set of numbers that covers all these intervals is {3, 6}.
'''

List_interval = [ [0, 3], [2, 6], [3, 4], [6, 9] ]

def smallest_cover(List_interval):
    mini = List_interval[0][1]
    maxi = List_interval[0][0]
    
    lenn=len(List_interval)
    for i in range(1,lenn):
        mini=min(mini,List_interval[i][1])
        maxi=max(maxi,List_interval[i][0])
    
    return {mini,maxi}