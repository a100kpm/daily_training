'''
Good morning! Here's your coding interview problem for today.

This problem was asked by LinkedIn.

Determine whether a tree is a valid binary search tree.

A binary search tree is a tree with two children, left and right, 
and satisfies the constraint that the key in the left child must be less than or equal 
to the root and the key in the right child must be greater than or equal to the root.
'''


class Tree:
    
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
        
tree=Tree(10)
tree.left=Tree(7)
tree.right=Tree(11)
tree.left.left=Tree(5)
tree.left.right=Tree(8)


def valid_tree(tree):
    a=True
    b=True
    d=True
    e=True
    val=tree.data
    if tree.left:
        if tree.left.data>val:
            a=False
        d=valid_tree(tree.left)
        
    if tree.right:
        if tree.right.data<val:
            b=False
        e=valid_tree(tree.right)
    
    c = a and b
    f = d and e
    g = f and c
    return g