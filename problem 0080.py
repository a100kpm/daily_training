'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given the root of a binary tree, return a deepest node. For example, in the following tree, return d.

    a
   / \
  b   c
 /
d
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

def deepest_node(Tree,compteur=0):
    val=Tree.data
    compteur+=1
    
    if Tree.right:
        valR,compteurR=deepest_node(Tree.right,compteur)
    else:
        compteurR=0
    if Tree.left:
        valL,compteurL=deepest_node(Tree.left,compteur)
    else:
        compteurL=0
    if compteurR == 0 and compteurL == 0:
        return val,compteur
    if compteurR>compteurL:
        return valR,compteurR
    return valL,compteurL
    
    