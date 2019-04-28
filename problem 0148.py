'''Good morning! Here's your coding interview problem for today.

This problem was asked by Apple.

Gray code is a binary code where each successive value differ in only one bit,
 as well as when wrapping around. Gray code is common in hardware so 
 that we don't see temporary spurious values during transitions.

Given a number of bits n, generate a possible gray code for it.

For example, for n = 2, one gray code would be [00, 01, 11, 10].
'''



def mouvement(n):
    mouv=[[1,2]]

    for i in range(1,n):
        a=mouv[i-1][0]*2
        b=mouv[i-1][1]*2
        mouv.append([a,b])
        
    return mouv

def find_pos_to_move(nbr,mouv):
    lenn=len(mouv)
    
    for i in range(lenn-1,-1,-1):
        if nbr%mouv[i][1]==mouv[i][0]:
            return i
    print(nbr)
    print(mouv)
    print('nothing to return')
    

def gray_bit2(n):
    List=[]
    List.append([0]*n)
    mouv=mouvement(n)
    list_temp=[0]*n
    for i in range(1,2**n):

        fp=find_pos_to_move(i,mouv)
        list_temp[fp]=(list_temp[fp]+1)%2
        List.append(list_temp)
        list_temp=list_temp.copy()
        
    return List