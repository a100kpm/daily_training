'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Atlassian.

MegaCorp wants to give bonuses to its employees based on how many lines of codes 
they have written. They would like to give the smallest positive amount to each worker
 consistent with the constraint that if a developer has written more lines of code than their neighbor,
 they should receive more money.

Given an array representing a line of seats of employees at MegaCorp, determine how much each one should get paid.

For example, given [10, 40, 200, 1000, 60, 30], you should return [1, 2, 3, 4, 2, 1].
'''

List = [10, 40, 200, 1000, 60, 30]
List2 = [30,60,1000,200,40,10]

def min_bonus(List):
    sub_list_indice=[]
    
    if List[1]>List[0]:
        direction=1
    else:
        direction=-1
        
    start_indice=0
    
    lenn=len(List)
    
    for i in range(1,lenn):
        if (List[i]-List[i-1])*direction>1:
            pass
        else:
            sub_list_indice.append([direction,start_indice,i-1])
            start_indice=i-1
            direction*=-1
    
    sub_list_indice.append([direction,start_indice,i])
    
    
    new_list=[0]*lenn
    
    for i,j,k in sub_list_indice:
        if i==1:
            compteur=1
            for l in range(j,k+1):

                new_list[l]=max(compteur,new_list[l])
                compteur+=1
        
        if i==-1:
            compteur=1
            for l in range(k,j-1,-1):

                new_list[l]=max(compteur,new_list[l])
                compteur+=1

                    
    return new_list