'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Glassdoor.

An imminent hurricane threatens the coastal town of Codeville. 
If at most two people can fit in a rescue boat, and the maximum weight limit 
for a given boat is k, determine how many boats will be needed to save everyone.

For example, given a population with weights [100, 200, 150, 80] and a boat 
limit of 200, the smallest number of boats required will be three. 
'''


array = [100, 200, 150, 80]

def num_boat(array,num=0,weight=200):
    if len(array)==0:
        return num
    if len(array)==1:
        return num+1
    
    lenn=len(array)
    val=array[0]
    result=[]
    result.append(num_boat(array[1:],num+1))
    for i in range(1,lenn):
        array_temp=array.copy()
        if val+array[i]<=weight:
            del(array_temp[i])
            result.append(num_boat(array_temp[1:],num+1))
    
    return min(result)