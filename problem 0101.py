'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Alibaba.

Given an even number (greater than 2), return two prime numbers whose sum will be equal to the given number.

A solution will always exist. See Goldbach’s conjecture.

Example:

Input: 4
Output: 2 + 2 = 4

If there are more than one solution possible, return the lexicographically smaller solution.

If [a, b] is one solution with a <= b, and [c, d] is another solution with c <= d, then

[a, b] < [c, d]

If a < c OR a==c AND b < d.
'''
import math

def find_sommeur_prime(input_):
    List_prime=[2]
    for i in range(3,input_,2):
        a=isprime(i)
        if a!=None:
            List_prime.append(a)
    
    lenn=len(List_prime)
    i=-1
    j=0
    done=False
    while j<lenn-1 and done==False:
        i+=1
        if i==lenn:
            i=0
            j+=1
        if List_prime[i]+List_prime[j]==input_:
            print("{} + {} = {}".format(List_prime[i],List_prime[j],input_))
            done=True
            
def isprime(i):
    max_test=math.floor(math.sqrt(i))+1
    
    for j in range(2,max_test):
        if i%j==0:
            return None
    return i