'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Given an integer N, construct all possible binary search trees with N nodes.
'''

class Tree:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
        
        
    def __repr__(self):
        node=self
        result = '['+str(node.val) + ' left:' + str(node.left)+ ' right:' + str(node.right)+'] '
        return result



def create_all_tree(N):
    if N==1:
        return [Tree(1)]
    if N==0:
        return [None]
    
    List_tree=[]
    for i in range(N):

        left=create_all_tree(i)
        right=create_all_tree(N-1-i)
        for j in left:
            for k in right:
                a=Tree(N)
                a.left=j
                a.right=k
                List_tree.append(a)
    return List_tree
    
        
        
    