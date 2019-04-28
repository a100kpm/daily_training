# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 17:20:37 2018

@author: iannis
"""

''' 
3/4 draw
1/6 win
1/12 loss

first with two win in a row = winner

proba of win ?
'''
import random

win = 2/12
loss = 1/12
draw = 9/12

def winner():
    w=0
    l=0
    
    while w!=2 and l!=2:
        game=random.randrange(1,13)
        if game==1:
            l+=1
            w=0
        elif game==2 or game==3:
            l=0
            w+=1
        else:
            w=0
            l=0
    if w==2:
        return 1
    return 0

def winner2():
    w=0
    l=0
    
    while w!=2 and l!=2:
        game=random.randrange(1,13)
        if game==1:
            l+=1
            w=0
        elif game==2 or game==3:
            l=0
            w+=1
    if w==2:
        return 1
    return 0

compteur=0
compteur2=0
for i in range(1000000):
    compteur+=winner()
    compteur2+=winner2()