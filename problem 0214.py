'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Stripe.

Given an integer n, return the length of the longest consecutive run of 1s in its binary representation.

For example, given 156, you should return 3.
'''
import math

def longest_one(number):
    result=0
    compteur=0
    while number > 0:
        if number%2==1:
            compteur+=1
            number=math.floor(number/2)
        else:
            if compteur>result:
                result = compteur
            compteur=0
            number=math.floor(number/2)
            
    if compteur>result:
        result = compteur
            
    return result


#10011100
#156
#01111111
#127