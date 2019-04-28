'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Apple.

Given the root of a binary tree, find the most frequent subtree sum. The subtree sum of a node is the sum of all values under a node, including the node itself.

For example, given the following tree:

  5
 / \
2  -5

Return 2 as it occurs twice: once as the left leaf, and once as the sum of 2 + 5 - 5.
'''

class tree:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
a=tree(5)
a.left=tree(2)
a.right=tree(-5)
a.right.right=tree(-5)
a.right.left=tree(5)
a.right.right.right=tree(-5)
a.right.right.left=tree(5)

def sum_tree(tree):
    List=[]
    a=0
    c=0
    if tree.left:
        a,b=sum_tree(tree.left)
        List.extend(b)
    if tree.right:
        c,d=sum_tree(tree.right)
        List.extend(d)
        
    som=a+c+tree.val
    List.append(som)
    return som,List

def find_max_sub_sum(tree):
    _,List=sum_tree(tree)
    
    dictio=dict()
    lenn=len(List)
    for i in range(lenn):
        if List[i] not in dictio:
            dictio[List[i]]=1
        else:
            dictio[List[i]]+=1
    
    return max(dictio,key=dictio.get)