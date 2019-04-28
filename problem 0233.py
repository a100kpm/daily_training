'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Apple.

Implement the function fib(n), which returns the nth number in the Fibonacci sequence, using only O(1) space.
'''

def fib(n):
    if n<=2:
        return 1
    else:
        num_1=1
        num_2=1
        for i in range(2,n):
            num=num_1+num_2
            num_1=num_2
            num_2=num
            
    return num