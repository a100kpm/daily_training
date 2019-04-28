'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Square.

In front of you is a row of N coins, with values v1, v1, ..., vn.

You are asked to play the following game. You and an opponent take turns choosing 
either the first or last coin from the row, removing it from the row, and receiving the value of the coin.

Write a program that returns the maximum amount of money you can win with certainty, 
if you move first, assuming your opponent plays optimally.
'''

import random

def generate_List_Vn(n,val_min=1,val_max=10):
    List_Vn=[]
    val_max=val_max+1
    for i in range(n):
        List_Vn.append(random.randrange(val_min,val_max))
        
    return List_Vn

List_Vn = [6,9,1,6,1,5,1,10,2,2]


def max_output(List_Vn,player=1,score1=0,score2=0):
    if len(List_Vn)==1:
        if player==1:
            return score1+List_Vn[0],score2
        else:
            return score1,score2+List_Vn[0]
        
        
    if player==1:
        score1_debut,score2_debut=max_output(List_Vn[1:],2,score1+List_Vn[0],score2)
        score1_fin,score2_fin=max_output(List_Vn[:-1],2,score1+List_Vn[-1],score2)
        
        if score1_debut>=score1_fin:
            return score1_debut,score2_debut
        return score1_fin,score2_fin
        
    else:
        score1_debut,score2_debut=max_output(List_Vn[1:],1,score1,score2+List_Vn[0])
        score1_fin,score2_fin=max_output(List_Vn[:-1],1,score1,score2+List_Vn[-1])
        
        if score2_debut>=score2_fin:
            return score1_debut,score2_debut
        return score1_fin,score2_fin