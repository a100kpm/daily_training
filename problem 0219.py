'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Salesforce.

Connect 4 is a game where opponents take turns dropping red or black discs 
into a 7 x 6 vertically suspended grid. The game ends either when one player
 creates a line of four consecutive discs of their color (horizontally, vertically,
 or diagonally), or when there are no more spots left in the grid.

Design and implement Connect 4.
'''
import numpy as np

class board():
    def __init__(self):
        self.play_board=np.array([' ']*42).reshape(6,7)
        
        self.column=range(1,8)
        self.high_max=6
        self.col_high=[self.high_max-1]*len(self.column)
        
        
        
        
    def add_pion(self,player,column):
        pos=[-1,-1]
        if column not in self.column:
            print('out of the board')
            return False,pos
        if self.col_high[column-1]<0:
            print('column is full')
            return False,pos
        
        if player==1:
            symbol='x'
        else:
            symbol='o'
            
        
        pos=[self.col_high[column-1],column-1]
        
        self.play_board[self.col_high[column-1]][column-1]=symbol
        self.col_high[column-1]-=1
        return True,pos
    
    
    def check_win(self,pos,player):
        if player==1:
            symbol='x'
        else:
            symbol='o'
            
        border_verti=range(0,6)
        border_hori=range(0,7)
        
        checker=[ 
            [ [pos[0]-3,pos[1]],[pos[0]-2,pos[1]],[pos[0]-1,pos[1]],[pos[0],pos[1]] ],
            [ [pos[0]-2,pos[1]],[pos[0]-1,pos[1]],[pos[0],pos[1]],[pos[0]+1,pos[1]] ],
            [ [pos[0]-1,pos[1]],[pos[0],pos[1]],[pos[0]+1,pos[1]],[pos[0]+2,pos[1]] ],
            [ [pos[0],pos[1]],[pos[0]+1,pos[1]],[pos[0]+2,pos[1]],[pos[0]+3,pos[1]] ],
            
            [ [pos[0]-3,pos[1]-3],[pos[0]-2,pos[1]-2],[pos[0]-1,pos[1]-1],[pos[0],pos[1]] ],
            [ [pos[0]-2,pos[1]-2],[pos[0]-1,pos[1]-1],[pos[0],pos[1]],[pos[0]+1,pos[1]+1] ],
            [ [pos[0]-1,pos[1]-1],[pos[0],pos[1]],[pos[0]+1,pos[1]+1],[pos[0]+2,pos[1]+2] ],
            [ [pos[0],pos[1]],[pos[0]+1,pos[1]+1],[pos[0]+2,pos[1]+2],[pos[0]+3,pos[1]+3] ],
            
            [ [pos[0],pos[1]-3],[pos[0],pos[1]-2],[pos[0],pos[1]-1],[pos[0],pos[1]] ],
            [ [pos[0],pos[1]-2],[pos[0],pos[1]-1],[pos[0],pos[1]],[pos[0],pos[1]+1] ],
            [ [pos[0],pos[1]-1],[pos[0],pos[1]],[pos[0],pos[1]+1],[pos[0],pos[1]+2] ],
            [ [pos[0],pos[1]],[pos[0],pos[1]+1],[pos[0],pos[1]+2],[pos[0],pos[1]+3] ],
            
            [ [pos[0]-3,pos[1]+3],[pos[0]-2,pos[1]+2],[pos[0]-1,pos[1]+1],[pos[0],pos[1]] ],
            [ [pos[0]-2,pos[1]+2],[pos[0]-1,pos[1]+1],[pos[0],pos[1]],[pos[0]+1,pos[1]-1] ],
            [ [pos[0]-1,pos[1]+1],[pos[0],pos[1]],[pos[0]+1,pos[1]-1],[pos[0]+2,pos[1]-2] ],
            [ [pos[0],pos[1]],[pos[0]+1,pos[1]-1],[pos[0]+2,pos[1]-2],[pos[0]+3,pos[1]-3] ],
            ]

        for i in range(16):
            compteur=0
            for j in range(4):
                
                if checker[i][j][0] in border_verti and checker[i][j][1] in border_hori:
                    if self.play_board[checker[i][j][0]][checker[i][j][1]]==symbol:
                        compteur+=1
                else:
                    break
            if compteur==4:
                print('player {} has win the game'.format(player))
                
                return True
        return False
            
    
def connect_four():
    a=board()
    
    player=1
    end=False
    turn = 0
    while end==False:
        print(a.play_board)
        print('player {} turns to play'.format(player))
        
        next_step=False
        while next_step==False:
            input_=input()
            input_=int(input_)
            next_step,pos=a.add_pion(player,input_)
        
        end = a.check_win(pos,player)
        if player==1:
            player=2
        else:
            player=1
        turn +=1
        
        if turn==42 and end==False:
            print('this is a draw')
            end=True
            
    print(a.play_board)
        
    
connect_four()
    
