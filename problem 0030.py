'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

You are given an array of non-negative integers that represents a 
two-dimensional elevation map where each element is unit-width wall and the integer is the height.
 Suppose it will rain and all spots between two walls get filled up.

Compute how many units of water remain trapped on the map in O(N) time and O(1) space.

For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.

Given the input [3, 0, 1, 3, 0, 5], 
we can hold 3 units in the first index, 2 in the second, 
and 3 in the fourth index (we cannot hold 5 since it would run off to the left), 
so we can trap 8 units of water.
'''

List= [3,0,1,3,0,5]

def stockage(List):
    
    lenn=len(List)
    water_tot=0
    water=0
    i=0
    while List[i+1]>List[i]:
        i+=1
    Current_wall=List[i]
    pos_current_wall=i    
    for j in range(1+i,lenn):
        if List[j]<Current_wall:
            water+=Current_wall-List[j]
        else:
            Current_wall=List[j]
            pos_current_wall=j
            water_tot+=water
            water=0
    if List[j]>=Current_wall:
        water_tot+=water
        return water_tot
    
    Current_wall=List[j]
    water=0
    for j in range(lenn-1,pos_current_wall,-1):
        water+=Current_wall-List[j]
    water_tot+=water
    
    return water_tot
        
    
    
            
        