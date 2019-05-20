'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

The game of Nim is played as follows. Starting with three heaps, each containing
 a variable number of items, two players take turns removing one or more items from a single pile. 
 The player who eventually is forced to take the last stone loses. For example, if the initial heap 
 sizes are 3, 4, and 5, a game could be played as shown below:

  A  |  B  |  C
-----------------
  3  |  4  |  5
  3  |  1  |  3
  3  |  1  |  3
  0  |  1  |  3
  0  |  1  |  0
  0  |  0  |  0 

In other words, to start, the first player takes three items from pile B. 
The second player responds by removing two stones from pile C. The game continues 
in this way until player one takes last stone and loses.

Given a list of non-zero starting values [a, b, c], and assuming optimal play, 
determine whether the first player has a forced win.
'''

List=[3,4,5]

def nim(List,player=1):
    List.sort(reverse=True)

    if (List[1]==0 and List[2]==0):
        return player
    
    if List[2]==0:
        if List[1]==1:
            return player
        if List[1]<List[0]:
            return player
        return (player+1)%2

    
    List_rez=[]
    player2=(player+1)%2
    for i in range(1,List[0]+1):
        List_rez.append(nim([List[0]-i,List[1],List[2]],player2))
    for i in range(1,List[1]+1):
        List_rez.append(nim([List[0],List[1]-i,List[2]],player2))
    for i in range(1,List[2]+1):
        List_rez.append(nim([List[0],List[1],List[2]-i],player2))
    if player in List_rez:
        return player
    return player2
    


    