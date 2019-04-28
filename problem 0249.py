'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Salesforce.

Given an array of integers, find the maximum XOR of any two elements.
'''

List = [5,6,7,7]


def max_xor(List):

#    List.remove(current_max)
    compteur=0
    while compteur==0:
        current_max=max(List)
        while max(List)==current_max:
            compteur+=1
            if len(List)==0:
                print('no sol')
                return
            List.remove(current_max)
            
        if compteur==1:
            return current_max
        else:
            compteur=0
            
    return current_max
            

def max_xor_duoelem(List):
    curr_max=max(List)
    curr_max2=min(List)
    
    lenn=len(List)
    for i in range(lenn):
        if List[i]!=curr_max and List[i]>curr_max2:
            curr_max2=List[i]
            
    
    return curr_max+curr_max2

print(max_xor_duoelem(List))
        
    

