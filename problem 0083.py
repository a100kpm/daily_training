'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Invert a binary tree.

For example, given the following tree:

    a
   / \
  b   c
 / \  /
d   e f

should become:

  a
 / \
 c  b
 \  / \
  f e  d
'''

class Node:
    def __init__(self,data):
        
        self.left = None
        self.right = None
        self.data = data
        
tree=Node('a')
tree.left=Node('b')
tree.left.left=Node('d')
tree.right=Node('c')
tree.left.right=Node('e')
tree.right.left=Node('f')


def tree_inverter(tree):
    a=tree.left
    tree.left=tree.right
    tree.right=a
    
    if tree.left:
        tree_inverter(tree.left)
    if tree.right:
        tree_inverter(tree.right)
        
    return tree
        