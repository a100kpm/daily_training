'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

A tree is symmetric if its data and shape remain unchanged when it is reflected about the root node. 
The following tree is an example:

        4
      / | \
    3   5   3
  /           \
9              9

Given a k-ary tree, determine whether it is symmetric.
'''
import math

class k_tree():
    def __init__(self,val,k=2,name='plop'):
        self.val=val
        self.kid=[None]*k
        self.k=k
        self.name=name
        
    
    def add_kid(self,val,pos,name):
        if pos>=self.k or pos<0:
            print('error position')
            return
        self.kid[pos]=k_tree(val,self.k,name) 
        
        
    
a=k_tree(4,3,'papa')
a.add_kid(3,0,'fils1')
a.add_kid(5,1,'fils2')
a.add_kid(3,2,'fils3')
a.kid[0].add_kid(9,0,'bebe1')
a.kid[2].add_kid(9,2,'bebe2')

def is_symetrical(tree1,tree2):
    if tree1!=None and tree2!=None:
        print(tree1.name)
        print(tree2.name)
        print('-------')
    if tree1==None and tree2==None:
        return True
    elif tree1!=None and tree2!=None:
        size=tree1.k
        nbr=math.floor(size/2)
        result=[]
        for i in range(nbr):
            if tree1.kid[i] and tree2.kid[size-i-1] or not tree1.kid[i] and not tree2.kid[size-i-1]:
                result.append(is_symetrical(tree1.kid[i],tree2.kid[size-i-1]))

        if size%2==1:
            result.append(is_symetrical(tree1.kid[i+1],tree2.kid[size-i-2]))
            
        for i in result:
            if i==False:
                return False
        return True


    else:
        return False