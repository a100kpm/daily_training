'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

Given a string and a pattern, find the starting indices of all occurrences of 
the pattern in the string. For example, given the string "abracadabra" and the 
pattern "abr", you should return [0, 7].
'''


word = "abracadabra"
pattern = "abr"


def pos_pattern(word,pattern):
    pos=[]
    lenn=len(word)
    lenn2=len(pattern)
    i=0
    
    while i<=lenn-lenn2:
        
        if word[i:i+lenn2]==pattern:
            pos.append(i)
            
        i+=1
        
    return pos
                
            
def pos_pattern2(word,pattern):
    pos=[]
    lenn=len(pattern)
    compteur=len(word)-len(pattern)+1
    for i in range(compteur):
        if word[i:i+lenn]==pattern:
            pos.append(i)
    return pos