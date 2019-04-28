'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

A number is considered perfect if its digits sum up to exactly 10.

Given a positive integer n, return the n-th perfect number.

For example, given 1, you should return 19. Given 2, you should return 28.
'''

def n_perfect(n):
    k=0
    i=0
    while k<n:
        i=i+1
        decompo=decomp(i)
        if decompo==10:
            k+=1
    return i

def decomp(i):
    score=0
    while i>9:
        score+=i%10
        i=i/10
        i=math.floor(i)
    score+=i    
    return score