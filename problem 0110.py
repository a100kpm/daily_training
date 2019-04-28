'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given a binary tree, return all paths from the root to leaves.

For example, given the tree

   1
  / \
 2   3
    / \
   4   5

it should return [[1, 2], [1, 3, 4], [1, 3, 5]].
'''


class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
a=Node(1)
a.left=Node(2)
a.right=Node(3)
a.right.left=Node(4)
a.right.right=Node(5)
resultat=[]

def show_path_in_tree(Tree,resultat,path=[],val=0):
    path.append(Tree.val)
    fin=True

    if Tree.left:
        fin=False
        show_path_in_tree(Tree.left,resultat,path.copy(),1)

    if Tree.right:
        fin=False
        show_path_in_tree(Tree.right,resultat,path.copy(),1)
        
    if fin==True:
        print(path)
        resultat.append(path)

    if val==0:
        return resultat