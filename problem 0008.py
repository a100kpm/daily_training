'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
'''

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
        
Node1=Node(1,Node(1),Node(1))
Node2=Node(0,Node1,Node(0))
tree = Node(0,Node(1),Node2)

def unival_subtree(tree):
    if not tree.left and not tree.right:
        return 1,True
    elif tree.left and not tree.right:
        nbr,subtree=unival_subtree(tree.left)
        if tree.left.val == tree.val and subtree==True:
            return nbr+1,subtree
        else:
            return nbr,False
    elif tree.right and not tree.left:
        nbr,subtree=unival_subtree(tree.right)
        if tree.right.val == tree.val and subtree==True:
            return nbr+1,subtree
        else:
            return nbr,False
    else:
        nbr_left,subtree_left=unival_subtree(tree.left)
        nbr_right,subtree_right=unival_subtree(tree.right)
        if not subtree_left or not subtree_right:
            return nbr_left+nbr_right,False
        elif tree.left.val == tree.right.val == tree.val and subtree_left==subtree_right:
            return nbr_left+nbr_right+1,True
        else:
            return nbr_left+nbr_right,False
            
        
    
            
        
        
        
