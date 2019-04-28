'''
Good morning! Here's your coding interview problem for today.

This question was asked by BufferBox.

Given a binary tree where all nodes are either 0 or 1,
 prune the tree so that subtrees containing all 0s are removed.

For example, given the following tree:

   0
  / \
 1   0
    / \
   1   0
  / \
 0   0

should be pruned to:

   0
  / \
 1   0
    /
   1

We do not remove the tree at the root or its left child because 
it still has a 1 as a descendant.
'''

class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
a = Node(0)
a.left = Node(1)
a.right= Node(0)
a.right.left=Node(1)
a.right.right=Node(0)
a.right.left.left=Node(0)
a.right.left.right=Node(0)


def remove_all_lone_zero(Tree,Tree_prec=None,side=None):
    if Tree.left:
        remove_all_lone_zero(Tree.left,Tree,'left')
    if Tree.right:
        remove_all_lone_zero(Tree.right,Tree,'right')
            
    if not Tree.left and not Tree.right and Tree.val==0:
            if side=='left':
                Tree_prec.left=None
            else:
                Tree_prec.right=None
    
            
    
