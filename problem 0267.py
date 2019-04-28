'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Oracle.

You are presented with an 8 by 8 matrix representing the positions of pieces on a chess board.
 The only pieces on the board are the black king and various white pieces. Given this matrix, 
 determine whether the king is in check.

For details on how each piece moves, see here.

For example, given the following matrix:

...K....
........
.B......
......P.
.......R
..N.....
........
.....Q..

You should return True, since the bishop is attacking the king diagonally.'''


import numpy as np
import random

chess = np.array([
                ['.','.','.','.','.','.','.','.'],
                ['.','.','.','.','.','.','.','.'],
                ['.','.','.','.','.','.','.','.'],
                ['.','.','.','.','.','.','.','.'],
                ['.','.','.','.','.','.','.','.'],
                ['.','.','.','.','.','.','.','.'],
                ['.','.','.','.','.','.','.','.'],
                ['.','.','.','.','.','.','.','.'],
                ])



def create_start(chess):
    King = (random.randrange(0,8),random.randrange(0,8))
    chess[King]='K'
    
    Q=random.randrange(0,2)
    B=random.randrange(0,3)
    R=random.randrange(0,3)
    N=random.randrange(0,3)
    P=random.randrange(0,9)
    while Q+B+R+N+P>0:
        a,b=random.randrange(0,8),random.randrange(0,8)
        while chess[a,b]!='.':
            a,b=random.randrange(0,8),random.randrange(0,8)
        if Q>0:
            Q-=1
            chess[a,b]='Q'
        elif B>0:
            B-=1
            chess[a,b]='B'
        elif R>0:
            R-=1
            chess[a,b]='R'
        elif N>0:
            N-=1
            chess[a,b]='N'
        elif P>0:
            if a==0:
                pass
            else:
                P-=1
                chess[a,b]='P'
            
    return chess

def check(chess):
    K=[np.where(chess=='K')[0][0],np.where(chess=='K')[1][0]]
    
    P=np.where(chess=='P')
    for i in range(np.shape(P)[1]):
        if P[0][i]==K[0]+1:
            if abs(P[1][i]-K[1])==1:
                print('check')
                return True
     
    R=np.where(chess=='R')
    for i in range(np.shape(R)[1]):
        if R[0][i]==K[0]:
            if abs(R[1][i]-K[1])==1:
                print('check')
                return True
            for j in range( min(R[1][i],K[1])+1 , max(R[1][i],K[1]) ):
                if chess[K[0],i]!='.':
                    break
                if j==max(R[1][i],K[1])-1:
                    print('check')
                    return True

        elif R[1][i]==K[1]:
            if abs(R[0][i]-K[0])==1:
                print('check')
                return True
            for i in range( min(R[0][i],K[0])+1 , max(R[0][i],K[0]) ):
                if chess[i,K[1]]!='.':
                    break
                if i==max(R[0][i],K[1])-1:
                    print('check')
                    return True
        
    B=np.where(chess=='B')
    for i in range(np.shape(B)[1]):
        if abs(B[0][i]-K[0])==abs(B[1][i]-K[1]):
            if abs(B[0][i]-K[0])==1:
                print('check')
                return True
            for j in range( min(B[0][i],K[0])+1,max(B[0][i],K[0])):
                for k in range( min(B[1][i],K[1])+1,max(B[1][i],K[1])):
                    if chess[j,k]!='.':
                        break
                    if j==max(B[0][i],K[0])-1:
                        print('check')
                        return True
        
        
    Q=np.where(chess=='Q')
    for i in range(np.shape(Q)[1]):
        if Q[0][i]==K[0]:
            if abs(Q[1][i]-K[1])==1:
                print('check')
                return True
            for i in range( min(Q[1][i],K[1])+1 , max(Q[1][i],K[1]) ):
                if chess[K[0],i]!='.':
                    break
                if i==max(Q[1][i],K[1])-1:
                    print('check')
                    return True

        elif Q[1][i]==K[1]:
            if abs(Q[0][i]-K[0])==1:
                print('check')
                return True
            for j in range( min(Q[0][i],K[0])+1 , max(Q[0][i],K[0]) ):
                if chess[i,K[1]]!='.':
                    break
                if j==max(Q[0][i],K[1])-1:
                    print('check')
                    return True
                
                
        if abs(Q[0][i]-K[0])==abs(Q[1][i]-K[1]):
            if abs(Q[0][i]-K[0])==1:
                print('check')
                return True
            for j in range( min(Q[0][i],K[0])+1,max(Q[0][i],K[0])):
                for k in range( min(Q[1][i],K[1])+1,max(Q[1][i],K[1])):
                    if chess[j,k]!='.':
                        break
                    if j==max(Q[0][i],K[0])-1:
                        print('check')
                        return True
        
    N=np.where(chess=='N')
    for i in range(np.shape(N)[1]):
        if abs(N[0][i]-K[0])+abs(N[1][i]-K[1])==3:
            if abs(N[0][i]-K[0])!=3 and abs(N[1][i]-K[1])!=3:
                print('check')
                return True
            
    print('no check')
    return False

chess=create_start(chess)
print(chess)
check(chess)
            