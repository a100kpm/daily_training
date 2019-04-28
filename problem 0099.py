'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example, given [100, 4, 200, 1, 3, 2], 
the longest consecutive element sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
'''

# O(n) impossible ? quid dans un cas ou n est extremement grand comparé a la taille de la liste initial ?

# Si l'on fait des sous list, et que l'on test les groupement a chaque itération, on a du O(n²) dans le pire des cas (voir O(n^3)?)

List=[100,4,200,1,3,2]

def max_consec(List):
    maxi=max(List)
    List_rez=[0]*(maxi+1)
    
    for i in List:
        List_rez[i]=1
        
    compteur=0
    compteur_max=0
    
    for i in List_rez:
        if i==1:
            compteur+=1
        else:
            compteur_max=max(compteur_max,compteur)
            compteur=0
    return compteur_max