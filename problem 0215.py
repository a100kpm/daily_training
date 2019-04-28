'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Yelp.

The horizontal distance of a binary tree node describes how far left or right 
the node will be when the tree is printed out.

More rigorously, we can define it as follows:

    The horizontal distance of the root is 0.
    The horizontal distance of a left child is hd(parent) - 1.
    The horizontal distance of a right child is hd(parent) + 1.

For example, for the following tree, hd(1) = -2, and hd(6) = 0.

             5
          /     \
        3         7
      /  \      /   \
    1     4    6     9
   /                /
  0                8

The bottom view of a tree, then, consists of the lowest node at each horizontal distance. 
If there are two nodes at the same depth and horizontal distance, either is acceptable.

For this tree, for example, the bottom view could be [0, 1, 3, 6, 8, 9].

Given the root to a binary tree, return its bottom view.
'''

class Tree:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
    def __repr__(self):
        return "Node[val={}]".format(self.val)
        
a=Tree(5)
a.left=Tree(3)
a.left.left=Tree(1)
a.left.left.left=Tree(0)
a.left.right=Tree(4)
a.right=Tree(7)
a.right.left=Tree(6)
a.right.right=Tree(9)
a.right.right.left=Tree(8)
        

def find_under_view(tree,pos=0,depth=0,list_view=[],list_pos=[],list_depth=[]):
    list_view1=[]
    list_view2=[]
    list_pos1=[]
    list_pos2=[]
    list_depth1=[]
    list_depth2=[]
    
    if pos in list_pos:
        position=list_pos.index(pos)
        list_view[position]=tree.val
    else:
        if len(list_pos)==0:
            list_pos.append(pos)
            list_view.append(tree.val)
            list_depth.append(depth)
        elif pos>max(list_pos):
            list_pos.append(pos)
            list_view.append(tree.val)
            list_depth.append(depth)
        else:
            list_pos.insert(0,pos)
            list_view.insert(0,tree.val)
            list_depth.insert(0,depth)
    
    if tree.left:
        list_view1,list_pos1,list_depth1=find_under_view(tree.left,pos-1,depth+1,list_view,list_pos,list_depth)
    
    if tree.right:
        list_view2,list_pos2,list_depth2=find_under_view(tree.right,pos+1,depth+1,list_view,list_pos,list_depth)
    
    if tree.left or tree.right:
        list_view,list_pos,list_depth=merge_list(list_view1,list_view2,list_pos1,list_pos2,list_depth1,list_depth2)
    
       
    return list_view,list_pos,list_depth


def merge_list(list_view1,list_view2,list_pos1,list_pos2,list_depth1,list_depth2):
    if len(list_view1)==0 and len(list_view2)!=0:
        return list_view2,list_pos2,list_depth2
    elif len(list_view2)==0 and len(list_view1)!=0:
        return list_view1,list_pos1,list_depth1
    
    mini1=min(list_pos1)
    mini2=min(list_pos2)
    max1=max(list_pos1)
    max2=max(list_pos2)
    max_global=max(max1,max2)
    mini_global=min(mini1,mini2)
    lenn=max_global-mini_global+1
    list_view=[0]*lenn
    list_pos=[0]*lenn
    list_depth=[0]*lenn
    i=0
    compteur=mini_global

    while i<lenn:
        depth1=-1
        depth2=-1
        if compteur in list_pos1:
            position1=list_pos1.index(compteur)
            depth1=list_depth[position1]
        if compteur in list_pos2:
            position2=list_pos2.index(compteur)
            depth2=list_depth[position2]
            
        if depth1>depth2:
            list_view[i]=list_view1[position1]
            list_pos[i]=list_pos1[position1]
            list_depth[i]=list_depth1[position1]
            
        else:
            list_view[i]=list_view2[position2]
            list_pos[i]=list_pos2[position2]
            list_depth[i]=list_depth2[position2]
            
        i+=1
        compteur+=1
        
    return list_view,list_pos,list_depth
            
            
result,_,_=find_under_view(a)
print(result)
#print(find_under_view(a)[0])
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
    
    
    
    
    