'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Yelp.

Given a mapping of digits to letters (as in a phone number), and a digit string,
 return all possible letters the number could represent. You can assume each valid number in the mapping is a single digit.

For example if {“2”: [“a”, “b”, “c”], 3: [“d”, “e”, “f”], …} then “23”
 should return [“ad”, “ae”, “af”, “bd”, “be”, “bf”, “cd”, “ce”, “cf"].
'''
import math
mapping = {2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4: ['g','h','i'], 5: ['j','k','l'], 6:
    ['m','n','o'], 7: ['p','q','r'], 8: ['s','t','u'], 9: ['v','w','x','y','z']}
    
#for i in range(len(mapping)):
#    for j in range(len(mapping[i+2])):
#        print(mapping[i+2][j])
        
nbr=23   
def decompo(nbr):
    List=[]
    List2=[]
    while nbr>0:
        List.append(nbr%10)
        nbr=math.floor(nbr/10)
    for i in range(len(List)-1,-1,-1):
        List2.append(List[i])
    return List2

def addeur(numerateur,Lister):
    lenn=len(numerateur)
    numerateur[-1]+=1
    for i in range(lenn-1,0,-1):
        if numerateur[i]>=len(Lister[i]):
            numerateur[i]=0
            numerateur[i-1]+=1
    return numerateur

def valid_mapping(mapping,nbr):
    List=decompo(nbr)
    
    lenn=len(List)
    Lister=[]
    for i in range(lenn):
        Lister.append(mapping[List[i]])
    combin_prepa=[]
    nbr_=1
    for i in range(len(Lister)):
        combin_prepa.append(len(Lister[i]))
        nbr_=nbr_*len(Lister[i])
        
    numerateur = [0]*len(combin_prepa)
    for i in range(nbr_):
        
        retour = ''
        for j in range(len(numerateur)):
            retour+=Lister[j][numerateur[j]]
        print(retour)
        print(numerateur)
        numerateur=addeur(numerateur,Lister)
        
        
valid_mapping(mapping,23)
        
        
        
        
    
    