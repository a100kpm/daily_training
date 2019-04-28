'''
Good morning! Here's your coding interview problem for today.

This problem was asked by MIT.

Blackjack is a two player card game whose rules are as follows:

    The player and then the dealer are each given two cards.
    The player can then "hit", or ask for arbitrarily many additional cards, so long as their total does not exceed 21.
    The dealer must then hit if their total is 16 or lower, otherwise pass.
    Finally, the two compare totals, and the one with the greatest sum not exceeding 21 is the winner.

For this problem, cards values are counted as follows: each card between 2 and 10 counts as their face value, 
face cards count as 10, and aces count as 1.

Given perfect knowledge of the sequence of cards in the deck, 
implement a blackjack solver that maximizes the player's score (that is, wins minus losses).
'''

import random

deck = dict()
card_name=set()
card_name.add('roi')
card_name.add('dame')
card_name.add('valet')
for i in range(1,11):
    card_name.add(str(i))
    
for i in card_name:
    deck[i]=4
    
    
number_deck=1

for i in deck:
    deck[i]=deck[i]*number_deck
    
    
def create_sequence(deck,number_deck=1):
    if number_deck>1:
        for i in deck:
            deck[i]=deck[i]*number_deck
            
    List=[]
    while len(deck)>0:
        prise=False
        
        while prise==False:
            choix = random.randrange(1,14)
            if choix==13:
                choix='roi'
                val=10
            elif choix==12:
                choix='dame'
                val=10
            elif choix==11:
                choix='valet'
                val=10
            else:
                choix=str(choix)
                val=int(choix)
            if choix in deck:
                List.append(val)
                deck[choix]-=1
                if deck[choix]==0:
                    deck.pop(choix)
                prise=True
    return List


def bank_play(List,point):
    while point<16:
        if len(List)==0:
            return 0,0,False
        point=point+List[0]
        List=List[1:]
    return List,point,True


def play_game(List,score=0):
    if len(List)<=4:
        return score
    
    point_joueur=List[0]+List[1]
    point_bank=List[2]+List[3]
    List=List[4:]
    
    val=[]
#    List_List=[]
    List_temp,point_temp,valid=bank_play(List,point_bank)
    if valid==True:
        if point_joueur<=21 and (point_joueur>point_temp or point_temp>21):
            val.append(play_game(List_temp,score+1))
        elif point_temp<=21 and (point_temp>point_joueur or point_joueur>21):
            val.append(play_game(List_temp,score-1))
        else:
            val.append(play_game(List_temp,score)) 
            
    while point_joueur<21 and len(List)>0:
        point_joueur+=List[0]
        List=List[1:]
        List_temp,point_temp,valid=bank_play(List,point_bank)
        if valid==True:
#            List_List.append(List_temp)
            if point_joueur<=21 and (point_joueur>point_temp or point_temp>21):
                val.append(play_game(List_temp,score+1))
            elif point_temp<=21 and (point_temp>point_joueur or point_joueur>21):
                val.append(play_game(List_temp,score-1))
            else:
                val.append(play_game(List_temp,score))
    if len(val)==0:
        return score
    return max(val)
    
    
List=create_sequence(deck,1)

print(play_game(List))
    
    
    
    
    
    
    
    
    
    
    
    