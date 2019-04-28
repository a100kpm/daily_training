'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Suppose you are given two lists of n points, one list p1, p2, ..., pn
 on the line y = 0 and the other list q1, q2, ..., qn on the line y = 1.
 Imagine a set of n line segments connecting each point pi to qi.
 Write an algorithm to determine how many pairs of the line segments intersect.
'''

def number_intersect(n):
    result=0
    
    for i in range(n):
        for j in range(n):
            result+=i*(n-j-1)

            result+=(n-i-1)*(j)

    return result/2