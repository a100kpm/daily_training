'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Netflix.

Given a sorted list of integers of length N, determine if an element x is in the 
list without performing any multiplication, division, or bit-shift operations.

Do this in O(log N) time.
'''

# can create a function that divide using only sum/substraction and then do a
# casual dichotomy
List = [1234,1235,1236,1237,1238,1239,1240,1242,1243,1244,1245,1246]

# This one seems O(log N) empirically, but no proof of it.
# It is some kind of reverse dichotomy


def is_n_in_list(List,n,compteur=0):
    pos=0
    List_pos=[0]
    move=1
    lenn = len(List)
    if lenn==0:
        return False
    if lenn==1:
        if List[0]==n:
            return True,compteur
        else:
            return False,compteur
    while pos<lenn-1: 
        if n==List[pos]:
            return True,compteur
        elif n>List[pos]:
            pos+=move
            List_pos.append(pos)
            move+=move            
        elif n<List[pos]:
            if len(List_pos)==1:
                return False,compteur
            else:
                return is_n_in_list(List[List_pos[-2]:List_pos[-1]],n,compteur+1)
        compteur+=1

        
    return is_n_in_list(List[List_pos[-2]+1:],n,compteur+1)
        

def is_in_list(List,n):
    if n<List[0]:
        return False,1
    return is_n_in_list(List,n,1)

for i in range(1230,1250):
    print('i=',i,' result = ', is_in_list(List,i))
    
# =============================================================================
# test zone
# =============================================================================
# import random
# aaa=[0]
# test_val=400000
# for i in range(1,test_val):
#     if random.randrange(0,2)==0:
#         aaa.append(i)
#         
# print(len(aaa))
# score_max=0
# score_tot=0
# for i in range(1,test_val):
#     _,score=is_in_list(aaa,i)
#     if score>score_max:
#         score_max=score
#     score_tot+=score
#     
# score_tot=score_tot*1.0/test_val
# =============================================================================
