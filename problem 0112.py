'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Twitter.

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree. 
Assume that each node in the tree also has a pointer to its parent.
'''


#   1
#  / \
# 2   3
#    / \
#   4   5

class Node:
    def __init__(self,val,prec):
        self.val=val
        self.left=None
        self.right=None
        self.prec=prec
        
        
a=Node(1,None)
a.left=Node(2,a)
a.right=Node(3,a)
a.right.left=Node(4,a.right)
a.right.right=Node(5,a.right)


def find_lca(Node1,Node2):
    List1=ancestor(Node1)
    List2=ancestor(Node2)
    lenn=len(List1)
    lenn2=len(List2)
    if List1[-1]!=List2[-1]:
        print('no common ancester')
        return None
    i=-1
    while List1[i]==List2[i]:
        i-=1
        if abs(i)>lenn or abs(i)>lenn2:
            return List1[i+1]
    return List1[i+1]


def ancestor(Node):
    List=[]
    father=Node
    List.append(father.val)
    while father.prec:
        father=father.prec
        List.append(father.val)
    return List