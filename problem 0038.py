'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

You have an N by N board. Write a function that, given N, 
returns the number of possible arrangements of the board where N queens 
can be placed on the board without threatening each other, i.e. 
no two queens share the same row, column, or diagonal.
'''

N=4

def number_position(N,Ban_list=[],Current_val=0):
    value=0
    if len(Ban_list)==0:
        for i in range(N):
            Ban_list.append([])
            
    
    Current_ban=[]
    lenn=len(Ban_list[Current_val])

    for j in range(lenn):
        if Ban_list[Current_val][j] in Current_ban:
            pass
        else:
            Current_ban.append(Ban_list[Current_val][j])
    Current_val+=1

    

    
    if Current_val<N-1:
        for i in range(N):
            if i in Current_ban:
                pass
            else:
                Ban=Ban_list[:]
                new_Ban_List=add_ban(Ban,Current_val,i,N)
                value+=number_position(N,new_Ban_List,Current_val)


    elif len(Current_ban)==N:
        return 0
    
    elif Current_val==N and len(Current_ban)<N:
        return 1    

    
    return value


def add_ban(Ban_list,Current_val,i,N):
    valeur1=i
    valeur2=i
    valeur3=i
    for j in range(Current_val,N):
        Ban_list[j].extend([valeur1])
        if valeur2<valeur1 and valeur2>=0:
            Ban_list[j].extend([valeur2])
        if valeur3>valeur1 and valeur3<N:
            Ban_list[j].extend([valeur3])
        valeur2-=1
        valeur3+=1
    return Ban_list