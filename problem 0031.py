'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

The edit distance between two strings refers to the minimum number 
of character insertions, deletions, and substitutions required to change 
one string to the other. For example, the edit distance between 
“kitten” and “sitting” is three: substitute the “k” for “s”, 
substitute the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them.
'''
import numpy as np

string1="kitten"
string2="sitting"

string11="kiette"


def distance_string(string1,string2):
    lenn1=len(string1)
    lenn2=len(string2)
    if lenn2<lenn1:
        string3=string2
        string2=string1
        string1=string3
        lenn1=len(string1)
        lenn2=len(string2)
        
    position = np.zeros([lenn1+1,lenn2+1])
    for i in range(lenn1+1):
        position[i,0]=i
    for j in range(lenn2+1):
        position[0,j]=j
        
    for i in range(1,lenn1+1):
        for j in range(1,lenn2+1):
            cout_sub=0
            if string1[i-1]!=string2[j-1]:
                cout_sub=1
            position[i,j]=min(position[i-1,j]+1,position[i,j-1]+1,position[i-1,j-1]+cout_sub)
    
    
    distance = position[i,j]
                
                
    return distance
            

