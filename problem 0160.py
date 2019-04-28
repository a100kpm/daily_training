'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Uber.

Given a tree where each edge has a weight, compute the length of the longest path in the tree.

For example, given the following tree:

   a
  /|\
 b c d
    / \
   e   f
  / \
 g   h

and the weights: a-b: 3, a-c: 5, a-d: 8, d-e: 2, d-f: 4, e-g: 1, e-h: 1, 
the longest path would be c -> a -> d -> f, with a length of 17.

The path does not have to pass through the root, and each node can have any amount of children.
'''

class tree():
    def __init__(self,val):
        self.val = val
        self.son=[]
    
    def add_son(self,val):
        self.son.append(tree(val))
        
tr=tree(0)
tr.add_son(3)
tr.add_son(5)
tr.add_son(8)
tr.son[2].add_son(2)
tr.son[2].add_son(4)
tr.son[2].son[0].add_son(1)
tr.son[2].son[0].add_son(1)
            

def longest_path(tree,List=[],start=0):
    if tree.son==[]:
        return tree.val
    
    lenn=len(tree.son)
    
    val=[]
    for i in range(lenn):
        val.append(longest_path(tree.son[i],List,start=1))
        
    max_val=max(val)
    if lenn>=2:
        index=val.index(max_val)
        val[index]=0
        max_val2=max(val)
        List.append(max_val+max_val2+tree.val)
    if start==1:
        return max_val+tree.val
    
    if start==0:
        return_max=max(val)
        return_max2=max(List)
        print(List)
        return max(return_max,return_max2)
    