'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

You are given an M by N matrix consisting of booleans that represents a board.
 Each True boolean represents a wall. Each False boolean represents a tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate, 
return the minimum number of steps required to reach the end coordinate from the start.
 If there is no possible path, then return null. You can move up, left, down, and right. 
 You cannot move through walls. You cannot wrap around the edges of the board.

For example, given the following board:

[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]

and start = (3, 0) (bottom left) and end = (0, 0) (top left), 
the minimum number of steps required to reach the end is 7, 
since we would need to go through (1, 2) because there is a wall everywhere else on the second row.
'''


import numpy as np

f=-1
t=-2
board = np.array([[f, f, f, f],
                  [t, t, f, t],
                  [f, f, f, f],
                  [f, f, f, f]])

start = (3,0)
end = (0,0)

def possible(x,y,lenn,lenn2):
    if x<0:
        return False
    if y<0:
        return False
    if x>=lenn:
        return False
    if y>=lenn2:
        return False
    return True

def path_min(board,start,end):
    lenn=np.shape(board)[0]
    lenn2=np.shape(board)[1]
    board[start]=0
    List_depart=[start]
#    List_ignore=[]
    while board[end]==-1:
        pos=List_depart[0]
        val=board[List_depart[0]]
        
#        List_ignore=List_depart[0]
        List_depart.remove(List_depart[0])
        x=pos[0]
        y=pos[1]
        
        if possible(x-1,y,lenn,lenn2):
            if board[x-1,y]==-1 or board[x-1,y]>val+1:
                board[x-1,y]=val+1
                List_depart.append((x-1,y))
            
        if possible(x+1,y,lenn,lenn2):
            if board[x+1,y]==-1 or board[x+1,y]>val+1:
                board[x+1,y]=val+1
                List_depart.append((x+1,y))
            
        if possible(x,y+1,lenn,lenn2):
            if board[x,y+1]==-1 or board[x,y+1]>val+1:
                board[x,y+1]=val+1
                List_depart.append((x,y+1))
            
        if possible(x,y-1,lenn,lenn2):
            if board[x,y-1]==-1 or board[x,y-1]>val+1:
                board[x,y-1]=val+1
                List_depart.append((x,y-1))
        
    return board[end]
        
        
    