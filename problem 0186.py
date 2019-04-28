'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

Given an array of positive integers, divide the array into two subsets such that
 the difference between the sum of the subsets is as small as possible.

For example, given [5, 10, 15, 20, 25], return the sets {10, 25} and {5, 15, 20},
 which has a difference of 5, which is the smallest possible difference.
'''

List=[5,10,15,20,25]

def divide_into_equal_set(List):
    total=sum(List)
    
    aim=total*1.0/2
    
    
    
    set_1,aim=create_set(List,aim)
    set_2=List.copy()
    i=0
    dictio=dict()
    lenn=len(set_1)
    for i in range(lenn):
        if set_1[i] in dictio:
            dictio[set_1[i]]+=1
        else:
            dictio[set_1[i]]=1
    i=0
    while i<len(set_2):
        if set_2[i] in dictio:
            dictio[set_2[i]]-=1
            if dictio[set_2[i]]==0:
                del dictio[set_2[i]]
            set_2.remove(set_2[i])
        else:
            i+=1
            
    
    
    return set_1,set_2,aim*2


def create_set(List,aim,set_=[]):    

    
    if len(List)==0:
        return set_,aim
    
    if List[0]<=aim:

        set_1,aim_1=create_set(List[1:],aim,set_)
        set_2=set_.copy()
        set_2.append(List[0])
        set_2,aim_2=create_set(List[1:],aim-List[0],set_2)
        
        if aim_1<aim_2:
            return set_1,aim_1
        else:
            return set_2,aim_2
    
    return create_set(List[1:],aim,set_)
    
        