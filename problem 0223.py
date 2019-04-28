'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Palantir.

Typically, an implementation of in-order traversal of a binary tree has O(h) 
space complexity, where h is the height of the tree. Write a program to compute the in-order 
traversal of a binary tree using O(1) space.
'''


class Tree():
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
        
    def reverse(self,Tree):
        self.previous=Tree
        
        
    def reverse_all(self,start=0):
        if start==0:
            self.previous=None
            
        if self.left:
            self.left.reverse(self)
            self.left.reverse_all(1)
        if self.right:
            self.right.reverse(self)
            self.right.reverse_all(1)


def binary_transvers(Tree,direction=1,compteur=0,last=None):
#    direction = 1 --> botom left
#    direction = 2 --> botom right
#    direction = 3 --> top
#    input()
#    print('direction=',direction)
#    print('compteur=',compteur)
#    print('nbr=',Tree.val)
    
#    LAZY FIX ON
    if last==Tree.right and Tree.previous==None:
        return
#    LAZY FIX OFF
    if direction==1:
        print(Tree.val)
        if Tree.left:
            binary_transvers(Tree.left,1,compteur,Tree)
        else:
            direction=2
            
    if direction==2:
        if Tree.right:
            binary_transvers(Tree.right,1,compteur+1,Tree)
        else:
            direction=3
            
    if direction==3:
        if Tree.previous==None:
            return
        if compteur==0:
            binary_transvers(Tree.previous,2,compteur,Tree)
        else:
            binary_transvers(Tree.previous,3,compteur-1,Tree)
            
  
a=Tree(1)
b=Tree(5)
c=Tree(6)
d=Tree(7)
e=Tree(8)
f=Tree(9)
a.left=b
a.right=c
b.left=d
b.right=e
c.left=f
#    1
#  5   6
# 7 8 9

a.reverse_all()
binary_transvers(a)




    