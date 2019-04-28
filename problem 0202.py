'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Palantir.

Write a program that checks whether an integer is a palindrome. 
For example, 121 is a palindrome, as well as 888. 678 is not a palindrome. 
Do not convert the integer into a string.
'''

nbr1=121
nbr2=123454321
nbr3=678
nbr4=1234

def nbr_palindrome(nbr):
    if nbr<10:
        return True
    
    taille=0
    while nbr//10**taille>0:
        taille+=1
    taille-=1
    
    while nbr>9:
        if nbr%10!=nbr//10**taille:
            return False
        nbr=int((nbr-(nbr//10**taille*10**taille)-nbr%10)/10)
        taille-=2
        
    return True
        