'''
Good morning! Here's your coding interview problem for today.

This problem was asked by WhatsApp.

Given an array of integers out of order, determine the bounds of the smallest 
window that must be sorted in order for the entire array to be sorted. For example, 
given [3, 7, 5, 6, 9], you should return (1, 3).
'''


List=[3,7, 5, 6, 9]

def indice_pour_sort(List):
    
    lenn=len(List)
    
    for i in range(1,lenn):
        if List[i]<List[i-1]:
            break
    i_min=i-1
    
    if i_min==lenn-1:
        return 0,0
    
    for i in range(lenn-2,-1,-1):
        if List[i]>List[i+1]:
            break
    i_max=i+2
    new_val_max=i_max
    for j in range(i_max,-1,-1):
        if List[i_max]<List[j]:
            new_val_max=j
            
    new_val_min=i_min
    for j in range(i_min,lenn):
        if List[i_min]>List[j]:
            new_val_min=j
            
    
#    if new_val_min>new_val_max:
#        return 0,0
    return new_val_max,new_val_min

print(indice_pour_sort(List))