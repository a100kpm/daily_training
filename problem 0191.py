'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Stripe.

Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Intervals can "touch", such as [0, 1] and [1, 2], but they won't be considered overlapping.

For example, given the intervals (7, 9), (2, 4), (5, 8), return 1 as the last interval can be removed and the first two won't overlap.

The intervals are not necessarily sorted in any order.
'''

interval = [(7,9),(2,4),(5,8)]
import numpy as np

def number_to_del(interval):
    graph=make_intersect_graph(interval)
    
    
    
    
def make_intersect_graph(interval):
    lenn=len(interval)
    graph=np.zeros([lenn,lenn])
    
    for i in range(lenn):
        min1=interval[i][0]
        max1=interval[i][1]
        for j in range(lenn):
            if i==j:
                pass
            else:
                min2=interval[j][0]
                max2=interval[j][1]
                
                if (min1<max2 and max1>min2) or (min2<max1 and max2>min1):
                    graph[i][j]=1
                    
    return graph

def retire_elem(graph,pos):
    graph=np.delete(graph,pos,0)
    graph=np.delete(graph,pos,1)
    
    return graph