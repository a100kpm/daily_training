'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

A regular number in mathematics is defined as one which evenly divides some power of 60. 
Equivalently, we can say that a regular number is one whose only prime divisors are 2, 3, and 5.

These numbers have had many applications, from helping ancient Babylonians keep time to tuning instruments according to the diatonic scale.

Given an integer N, write a program that returns, in order, the first N regular numbers.
'''


def first_regular(N):
    result=[]
    i=1
    while len(result)<N:
        i+=1
        j=i
        while j%2==0:
            j/=2
        while j%3==0:
            j/=3
        while j%5==0:
            j/=5
        if j==1:
            result.append(i)
            
    return result