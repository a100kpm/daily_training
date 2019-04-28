'''
Good morning! Here's your coding interview problem for today.

This question was asked by ContextLogic.

Implement division of two positive integers without using the division, multiplication, 
or modulus operators. Return the quotient as an integer, ignoring the remainder.
'''

def division_restric(n1,n2):
    val = 0
    if n2==0:
        print('error')
        return None
    while n1>=n2:
        val+=1
        n1-=n2
    return val
