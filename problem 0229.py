'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Flipkart.

Snakes and Ladders is a game played on a 10 x 10 board, the goal of which is get from square 1 
to square 100. On each turn players will roll a six-sided die and move forward a number of spaces equal 
to the result. If they land on a square that represents a snake or ladder, 
they will be transported ahead or behind, respectively, to a new square.

Find the smallest number of turns it takes to play snakes and ladders.

For convenience, here are the squares representing snakes and ladders, and their outcomes:

snakes = {16: 6, 48: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
'''


snakes = {16: 6, 48: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}



def distance_for_each_case(snakes,ladders,changement=True,start_pos=0):
    List=[100]*101
    List[100]=0
    for i in range(99,-1,-1):
        if i in ladders:
            List[i]=List[ladders[i]]
            
        elif i in snakes:
            pass
        
        else:
            List[i]=1+min(List[i+1:i+7])
            
    for i in snakes:
        List[i]=List[snakes[i]]
        
#    changement=True
    compteur=-1

    while changement==True:
        compteur+=1
        changement=False
        for i in range(99,-1,-1):
            if i in ladders:
                if List[ladders[i]]!=List[i]:
                    changement=True
                List[i]=List[ladders[i]]
                
            elif i in snakes:
                pass
            
            else:
                val=List[i]
                List[i]=1+min(List[i+1:i+7])
                if val!=List[i]:
                    changement=True
        for i in snakes:
            if List[i]!=List[snakes[i]]:
                changement=True
            List[i]=List[snakes[i]]
    print('repetition=',compteur)
#    return List
    return List[start_pos]



# =============================================================================
# 0/1->38/44/50/51->67/73/79/80->100
# 
# +1 +6 +6 +1 +6 +6 +1
# =============================================================================
