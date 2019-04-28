'''
Good morning! Here's your coding interview problem for today.

This problem was asked by LinkedIn.

Given a string, return whether it represents a number. Here are the different kinds of numbers:

    "10", a positive integer
    "-10", a negative integer
    "10.1", a positive real number
    "-10.1", a negative real number
    "1e5", a number in scientific notation

And here are examples of non-numbers:

    "a"
    "x 1"
    "a -2"
    "-"
'''
#import math

def is_a_number(string):
    if len(string)!=1:
        if string[0]=='-':
            string=string[1:]
    if string[0]=='e' or string[0]=='.':
        return False
    string_ok='0123456789e.'
    lenn=len(string)
    countE=0
    posE=None
    posDot=None
    countDot=0
    for i in range(lenn):
        carac_courant=string[i]
        if carac_courant=='e':
            countE+=1
            posE=i
            if countE>1:
                return False
        if carac_courant=='.':
            countDot+=1
            posDot=i
            if countDot>1:
                return False
        if carac_courant not in string_ok:
            return False
    if posE and posDot:
        if abs(posE-posDot)==1:
            return False
    return True
            
    