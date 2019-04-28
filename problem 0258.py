'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Morgan Stanley.

In Ancient Greece, it was common to write text with the first line going left to right, 
the second line going right to left, and continuing to go back and forth. 
This style was called "boustrophedon".

Given a binary tree, write an algorithm to print the nodes in boustrophedon order.

For example, given the following tree:

       1
    /     \
  2         3
 / \       / \
4   5     6   7

You should return [1, 3, 2, 4, 5, 6, 7].
'''

class Tree():
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
    def __repr__(self):
        node=self
        result="["
        List_next=[node]
        order='left'
        
        while len(List_next)!=0:
            List_temp=[]
            lenn=len(List_next)
            if order=='left':
                for i in range(lenn):
                    new_node=List_next[i]
                    if new_node.left:
                        List_temp.append(new_node.left)
                    if new_node.right:
                        List_temp.append(new_node.right)
                    result+=str(new_node.val)
                    result+=","
                order='right'
            elif order=='right':
                for i in range(lenn-1,-1,-1):
                    new_node=List_next[i]
                    if new_node.right:
                        List_temp.insert(0,new_node.right)
                    if new_node.left:
                        List_temp.insert(0,new_node.left)
                    result+=str(new_node.val)
                    result+=","
                order='left'
                
            List_next=List_temp.copy()
            
        result=result[:-1]
        result+="]"
            
        return result
            
                
        
        
a=Tree(1)
b=Tree(2)
c=Tree(3)
d=Tree(4)
e=Tree(5)
f=Tree(6)
g=Tree(7)

a.left=b
a.right=c
b.left=d
b.right=e
c.left=f
c.right=g


print(a)
