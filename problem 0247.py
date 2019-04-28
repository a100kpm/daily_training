'''
Good morning! Here's your coding interview problem for today.

This problem was asked by PayPal.

Given a binary tree, determine whether or not it is height-balanced. 
A height-balanced binary tree can be defined as one in which the heights of 
the two subtrees of any node never differ by more than one.
'''
import math

class binary_tree():
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        

a=binary_tree(0)
b=binary_tree(1)
c=binary_tree(2)
d=binary_tree(3)
e=binary_tree(4)

a.left=b
a.right=c
b.left=d



def balance(Tree,balanced=True):
    c=balanced
    cc=balanced
    if Tree.left==None:
        val_gauche=0
    else:
        a,b,c=balance(Tree.left)
        val_gauche=max(a,b)+1
    if Tree.right==None:
        
        val_droite=0
    else:
        aa,bb,cc=balance(Tree.right)
        val_droite=max(aa,bb)+1
        
    if abs(val_gauche-val_droite)>1:
        balanced = False
        
    if c==False or cc==False:
        balanced = False
        
    return val_gauche,val_droite,balanced
        
    
        
print(balance(a)[2])
d.left=e
print(balance(a)[2])