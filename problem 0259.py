'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Two Sigma.

Ghost is a two-person word game where players alternate appending letters to a word. 
The first person who spells out a word, or creates a prefix for which 
there is no possible continuation, loses. Here is a sample game:

    Player 1: g
    Player 2: h
    Player 1: o
    Player 2: s
    Player 1: t [loses]

Given a dictionary of words, determine the letters the first player 
should start with, such that with optimal play they cannot lose.

For example, if the dictionary is ["cat", "calf", "dog", "bear"],
 the only winning start letter would be b. 
                 (faux, c marche aussi)
'''

List = ["cat", "calf", "dog", "bear"]


def win_letter(List,player=1,start=True):
    result=1
    for i in List:
        if len(i)%2!=0:
            result=0
    if result==1:
        if player==1:
            return result
        return -result
        
       
    result=[] 
    first_letter=[]
    
    for i in List:
        if i[0] not in first_letter:
            first_letter.append(i[0])
            
    for i in first_letter:
        temp_list=[]
        for j in List:
            if j[0]==i:
                temp_list.append(j[1:])
        result.append(win_letter(temp_list,-player,False))
        
    if start==False:
        if player==1:
            if 1 in result:
                return 1
            else:
                return -1
        if -1 in result:
            return -1
        return 1
    
    lenn=len(first_letter)
    for i in range(lenn):
        if result[i]==1:
            print(first_letter[i],'est gagnant')
        else:
            print(first_letter[i],'est non gagnant')
            
            
            
            
            
    




