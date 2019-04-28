'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Dropbox.

Given the root to a binary search tree, find the second largest node in the tree.
'''
import numpy as np
class Tree(object):
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None
        
        
a=Tree(20)
a.right=Tree(22)
a.left=Tree(8)
a.left.left=Tree(4)
a.left.right=Tree(12)
a.left.right.left=Tree(10)
a.left.right.right=Tree(14)
b=a.left.right
c=a.left

def make_list(node):
    List=[]
    List.append([node,node.data])

    if node.left!=None:
        List.extend(make_list(node.left))
        
    if node.right!=None:
        List.extend(make_list(node.right))
        
    return List
        

def find_2nd_biggest(node):
    List=make_list(node)
    List_val=[x[1] for x in List]
    index1=np.argmax(List_val)
    List_val=List_val[:index1]+List_val[(index1+1):]
    index2=np.argmax(List_val)
    
    if index2>=index1:
        index=index2+1
    else:
        index=index2
    
    return List[index]





