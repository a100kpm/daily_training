'''
Good morning! Here's your coding interview problem for today.

Given a real number n, find the square root of n. For example, given n = 9, return 3.
'''
import math

def square_root(n):
    time=10+math.floor(10*math.log(n))
    a=n
    for _ in range(time):
        b=a
        a=0.5*(a+n/a)
        calc=b-a
        print(calc)
        if calc==0:
            break
    return a

