'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Yahoo.

Recall that a full binary tree is one in which each node is either a leaf node, 
or has two children. Given a binary tree, convert it to a full one by removing nodes with only one child.

For example, given the following tree:

         0
      /     \
    1         2
  /            \
3                 4
  \             /   \
    5          6     7

You should convert it to:

     0
  /     \
5         4
        /   \
       6     7
'''

class Tree():
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
        
def binary(Tree,prec_=None,side=None):
    if side==None:
        if Tree.left and Tree.right:
            binary(Tree.left,Tree,'left')
            binary(Tree.right,Tree,'right')
        
        elif Tree.left and not Tree.right:
            Tree.left=None
        elif Tree.right and not Tree.left:
            Tree.right=None
            
    elif side=='left':
        if Tree.left and Tree.right:
            binary(Tree.left,Tree,'left')
            binary(Tree.right,Tree,'right')
            
        elif Tree.left and not Tree.right:
            prec_.left=Tree.left
            binary(Tree.left,prec_,'left')
            
        elif Tree.right and not Tree.left:
            prec_.left=Tree.right
            binary(Tree.right,prec_,'left')
            
    elif side=='right':
        if Tree.left and Tree.right:
            binary(Tree.left,Tree,'left')
            binary(Tree.right,Tree,'right')
            
        elif Tree.left and not Tree.right:
            prec_.right=Tree.left
            binary(Tree.left,prec_,'right')
            
        elif Tree.right and not Tree.left:
            prec_.right = Tree.right
            binary(Tree.right,prec_,'right')       
                
                
a=Tree(0)
b=Tree(1)
c=Tree(2)
d=Tree(3)
e=Tree(4)
f=Tree(5)
g=Tree(6)
h=Tree(7)

a.left=b
a.right=c
b.left=d
d.right=f
c.right=e
e.left=g
e.right=h

