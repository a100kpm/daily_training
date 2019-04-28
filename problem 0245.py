'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Yelp.

You are given an array of integers, where each element represents the maximum number of 
steps that can be jumped going forward from that element. Write a function to return the minimum number 
of jumps you must take in order to get from the start to the end of the array.

For example, given [6, 2, 4, 0, 5, 1, 1, 4, 2, 9], you should return 2, as 
the optimal solution involves jumping from 6 to 5, and then from 5 to 9.
'''

List_jump = [6, 2, 4, 0, 5, 1, 1, 4, 2, 9]


# méthode récursiv
def min_jump(List_jump,nbr=0):
    if len(List_jump)<=1:
        return nbr
    
    if List_jump[0]==0:
        return -1
    val=[]
    for i in range(1,List_jump[0]+1):
        
        val.append(min_jump(List_jump[i:],nbr+1))
        
    for x in val:
        if x==-1:
            val.remove(x)
            
    return min(val)


#méthode smart
def min_jump_start(List_jump):
    lenn=len(List_jump)
    List_pos=[lenn+1]*lenn
    List_pos[-1]=0
    
    for i in range(lenn-2,-1,-1):
        if List_jump[i]==0:
            pass
        else:
            List_pos[i]=min([x for x in List_pos[i:i+1+List_jump[i]]])+1
        
    return List_pos[0]
        