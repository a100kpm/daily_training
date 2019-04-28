'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Pinterest.

The sequence [0, 1, ..., N] has been jumbled, and the only clue you have for 
its order is an array representing whether each number is larger or smaller 
than the last. Given this information, reconstruct an array that is consistent with it. 
For example, given [None, +, +, -, +], you could return [1, 2, 3, 0, 4].
'''

List=[None, "+", "+", "-", "+"]
lenn=len(List)



def propose_array(List,lenn):
    compteur=0
    for i in List:
        if i=="+":
            compteur+=1
            
    nbr=lenn-compteur-1
    nbr2=nbr
    result=[nbr]
    
    for i in List[1:]:
        if i=="+":
            nbr2+=1
            result.append(nbr2)
        else:
            nbr-=1
            result.append(nbr)
            
    return result


print(propose_array(List,lenn))