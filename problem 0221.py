'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Zillow.

Let's define a "sevenish" number to be one which is either a power of 7, 
or the sum of unique powers of 7. The first few sevenish numbers are 1, 7, 8, 49, 
and so on. Create an algorithm to find the nth sevenish number.
'''


def generate_nth_sevenish(n):
    a=bin(n)
    lenn=len(bin(n))
    lenn1=lenn-2
    power=[]
    for i in range(lenn1):
        power.append(7**i)
    
    value=0
    for i in range(lenn-1,1,-1):
        if a[i]=='1':
            value+=power[lenn-1-i]
            
    return value