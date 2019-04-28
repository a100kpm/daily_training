'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Implement locking in a binary tree. A binary tree node can be locked or unlocked 
only if all of its descendants or ancestors are not locked.

Design a binary tree node class with the following methods:

    is_locked, which returns whether the node is locked
    lock, which attempts to lock the node. If it cannot be locked, then it should return false. 
    Otherwise, it should lock it and return true.
    unlock, which unlocks the node. If it cannot be unlocked, 
    then it should return false. Otherwise, it should unlock it and return true.

You may augment the node to add parent pointers or any other property you would like.
 You may assume the class is used in a single-threaded program, 
 so there is no need for actual locks or mutexes. Each method should run in O(h),
 where h is the height of the tree.
'''


class Tree:
    def __init__(self,data=None,left=None,right=None,parent=None):
        self.left = left
        self.right = right
        self.data = data
        self.parent = parent
        
    def add_son(self,data,side):
        if side=='left':
            self.left=Tree(data=data,parent=self)
        elif side=='right':
            self.right=Tree(data=data,parent=self)
            
            
            
    def is_locked(self,initial=True):
        compteur=0
        if self.data=='locked':
#            return True
            compteur=1
            if initial==True:
                compteur=compteur-0.5
        if initial==True:
            a=self.parent
            while a:
                if a.data=='locked':
#                    return True
                    compteur+=1
                a=a.parent
        if compteur>=1:
            return True
        if self.left!=None:
#            return self.left.is_locked(initial=False)
            compteur+= self.left.is_locked(initial=False)
        if self.right!=None:
#            return self.right.is_locked(initial=False)
            compteur+= self.right.is_locked(initial=False)
        if initial==False:
            return compteur
        if compteur>=1:
            return True
        return False
    
    def lock(self):
        if self.is_locked(initial=True)==False:
            self.data='locked'
            return True
        else:
            return False
    
    def unlock(self):
        if self.is_locked(initial=True)==False:
            self.data='unlocked'
            return True
        else:
            return False
        
        
    
root=Tree(data='unlocked')

root.add_son('unlocked','left')

a=root.left

a.add_son('unlocked','right')

b=a.right