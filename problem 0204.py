'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Given a complete binary tree, count the number of nodes in faster than O(n) time. 
Recall that a complete binary tree has every level filled except the last, 
and the nodes in the last level are filled starting from the left.
'''

'''
         0
       /  \
      1    2
     / \  / \
    3   4 5  6
   / \
  7   8
  
'''
import math

class Tree:

    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
        
a=Tree(0)
a.left=Tree(1)
a.left.left=Tree(3)
a.left.right=Tree(4)
a.right=Tree(2)
a.right.left=Tree(5)
a.right.right=Tree(6)
a.left.left.left=Tree(7)
a.left.left.right=Tree(8)


def num_to_binary(val,nbr_bin):
    List=[0]*nbr_bin
    div=2**(nbr_bin-1)
    pos=0
    while pos<=len(List)-1:
        if div<=val:
            val-=div
            List[pos]=1
        pos+=1
        div=div/2
        
    return List
        
            
    
def count_node(tree):
    compteur1=1
    compteur2=1
    a=tree
    b=tree
    
    while a.right:
        a=a.right
        compteur1+=1
    
    while b.left:
        b=b.left
        compteur2+=1
        
    score=2**compteur1-1
    
    if compteur1==compteur2:
        return score
    
    val1=0
    val2=2**compteur1-1
    val3=math.floor((val1+val2)/2)
    
    while val1!=val3:
        tree_temp=tree
        List_order=num_to_binary(val3,compteur1)
        result=1
        for i in range(compteur1):
            if List_order[i]==0:
                if tree_temp.left:
                    tree_temp=tree_temp.left
                else:
                    result=0

            else:
                if tree_temp.right:
                    tree_temp=tree_temp.right
                else:
                    result=0

            
        if result==1:
            val1=val3
            val3=math.ceil((val1+val2)/2)
            
        else:
            val2=val3
            val3=math.floor((val1+val2)/2)
            

    return score+val3+1
            
            
            
            
            
            
            
            
            
            
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    