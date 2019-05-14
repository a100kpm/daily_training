'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Yext.

Two nodes in a binary tree can be called cousins if they are on the same level 
of the tree but have different parents. For example, in the following diagram 4 and 6 are cousins.

    1
   / \
  2   3
 / \   \
4   5   6

Given a binary tree and a particular node, find all cousins of that node.
'''


class Tree():
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
    def __repr__(self):
        node=self
        return '['+ str(node.val) + ' left: '+str(node.left) + ' right: '+str(node.right)+']'
    
    def give_heigth(self,init_height=0):
        self.height=init_height
        if self.left:
            self.left.give_heigth(init_height+1)
        if self.right:
            self.right.give_heigth(init_height+1)
    
a=Tree(1)
b=Tree(2)
c=Tree(3)
d=Tree(4)
e=Tree(5)
f=Tree(6)

a.left=b
a.right=c
b.left=d
b.right=e
c.right=f

print(find_cousin(a,f))

def find_cousin(tree,node):
    tree.give_heigth()
    hauteur=node.height
    
    List=find_node_and_parents(tree,hauteur)
    lenn=len(List)
    for i in range(lenn):
        if List[i].left:
            if List[i].left==node:
                break
        if List[i].right:
            if List[i].right==node:
                break
            
    del(List[i])
    rez=[]
    for i in List:
        if i.left:
            rez.append(i.left)
        if i.right:
            rez.append(i.right)
            
    return rez
    
            
    
    
def find_node_and_parents(tree,hauteur):
    result=[]
    if tree.height==hauteur-1:
        return [tree]
    if tree.left:
        rezl=find_node_and_parents(tree.left,hauteur)
        result.extend(rezl)
    if tree.right:
        rezr=find_node_and_parents(tree.right,hauteur)
        result.extend(rezr)
        
    return result
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    