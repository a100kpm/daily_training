'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Pinterest.

Given an integer list where each number represents the number of hops you can make,
 determine whether you can reach to the last index starting at index 0.

For example, [2, 0, 1, 0] returns true while [1, 1, 0, 1] returns false.
'''

List1=[2,0,1,0]
List2=[1,1,0,1]
List3=[1,2,3,4,5,6,7,0,0,0,0,2,2,1,4,5,0,0,0,3,0,0,1,0]
#,6,7,0,0,0,0,2,2,1,4,5,0,0,0,3,0,0,1,0

def can_hope(List,pos=0):
    lenn=len(List)

    if pos>=lenn-1:
        return True
    
    val = List[pos]
    possible=[]
#    print(pos)
    for i in range(1,val+1):
        possible.append(can_hope(List,pos+i))
        
    if len(possible)==0:
        return False
#    print(pos)
#    print(possible)
    if any(possible):
        return True
    return False