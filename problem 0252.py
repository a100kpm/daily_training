'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Palantir.

The ancient Egyptians used to express fractions as a sum of several terms where
 each numerator is one. For example, 4 / 13 can be represented as 1 / 4 + 1 / 18 + 1 / 468.

Create an algorithm to turn an ordinary fraction a / b, where a < b, into an Egyptian fraction.
'''
import math


a=4
b=13
List=[]

a_=a
b_=b


    

    
def sub_fract(a,b,i):
    numerator=a*i-b
    denominator=b*i
    
    div=math.gcd(int(numerator),int(denominator))
    
    return numerator/div,denominator/div
    
    
while a_>1:
    val=a_/b_
    i=1
    while 1/i>val:
        i+=1

    List.append(i)
    
    a_,b_=sub_fract(a_,b_,i)
    
List.append(int(b_))

print(List)