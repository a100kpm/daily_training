'''
Good morning! Here's your coding interview problem for today.

This problem was asked by LinkedIn.

Given a set of characters C and an integer k, a De Bruijn sequence is a cyclic sequence 
in which every possible k-length string of characters in C occurs exactly once.

For example, suppose C = {0, 1} and k = 3. Then our sequence should contain the substrings 
{'000', '001', '010', '011', '100', '101', '110', '111'}, and one possible solution would be 00010111.

Create an algorithm that finds a De Bruijn sequence.
'''

# NOT THE SHORTEST VERSION
C = {0,1}

k=3


def create_all_set(C,k,val=''):
    if k==0:
        return {val}
    
    set_=set()

    for i in C:
        set_|=create_all_set(C,k-1,val+str(i))
         
    return set_
     
 
def dist_gauche(i,word):       
    lenn=len(i)
    dist=0
    for j in range(lenn-1,-1,-1):
        dist+=1
        if word[:j]==i[-j:]:
            break
    return i[:dist],dist

def dist_droite(i,word):
    lenn=len(i)
    dist=0
    for j in range(lenn-1,-1,-1):
        dist+=1
        if word[-j:]==i[:j]:
            break
        
    return i[-dist:],dist
        
def bruijn(C,k):
    all_set = create_all_set(C,k)
    
    word=all_set.pop()
    distance=0
    while len(all_set)>0:
        distance+=1

        
        for i in all_set:
            letter,dist=dist_gauche(i,word[:k])
            if dist==distance:
                word=letter+word
                all_set.remove(i)
                distance=0
                break
            letter,dist=dist_droite(i,word[-k:])
            if dist==distance:
                word=word+letter
                all_set.remove(i)
                distance=0
                break
                
            
    print(word)
            
                    

    
    