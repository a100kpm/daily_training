'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Netflix.

Given an array of integers, determine whether it contains a Pythagorean triplet.
 Recall that a Pythogorean triplet (a, b, c) is defined by the equation a2+ b2= c2.
'''

def pytha(a,b,c):
    if a>=b and a>=c:
        if a**2==b**2+c**2:
            return True
        return False
        
    elif b>=a and b>=c:
        if b**2==a**2+c**2:
            return True
        return False
    else:
        if c**2==a**2+b**2:
            return True
        return False