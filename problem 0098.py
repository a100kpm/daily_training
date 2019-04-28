'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Coursera.

Given a 2D board of characters and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where 
"adjacent" cells are those horizontally or vertically neighboring. 
The same letter cell may not be used more than once.

For example, given the following board:

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

exists(board, "ABCCED") returns true, 
exists(board, "SEE") returns true, 
exists(board, "ABCB") returns false.
'''

import numpy as np

board= np.array([
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
])


def exists(board,strr):
    List=[]
    lenn=np.shape(board)[0]
    lenn2=np.shape(board)[1]
    first_letter=strr[0]
    for i in range(lenn):
        for j in range(lenn2):
            
            if board[i][j]==first_letter:
                result = cherche_lettre(board,strr,i,j,List)
                if result == True:
                    return result
    return False

def cherche_lettre(board,strr,i,j,List=[]):
    lenn=np.shape(board)[0]
    lenn2=np.shape(board)[1]
    new_str=strr[1:]
    List.append([i,j])
#    print(List)
    result=False
    if len(new_str)==0:
        return True
    
    
    else:
        if i>0:
            if new_str[0]==board[i-1][j] and [i-1,j] not in List:
                result = cherche_lettre(board,new_str,i-1,j,List)
                if result==True:
                    return True
        if j>0:
            if new_str[0]==board[i][j-1] and [i,j-1] not in List:
                result = cherche_lettre(board,new_str,i,j-1,List)
                if result==True:
                    return True
                
        if i<lenn-1:
            if new_str[0]==board[i+1][j] and [i+1,j] not in List:
                result = cherche_lettre(board,new_str,i+1,j,List)
                if result==True:
                    return True
        
        if j<lenn2-1:
            if new_str[0]==board[i][j+1] and [i,j+1] not in List:
                result = cherche_lettre(board,new_str,i,j+1,List)
                if result==True:
                    return True
                
    return result
        