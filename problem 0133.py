'''
Good morning! Here's your coding interview problem for today.

This question was asked by Apple.

Given a binary tree, find a minimum path sum from root to a leaf.

For example, the minimum path in this tree is [10, 5, 1, -1], which has sum 15.

  10
 /  \
5    5
 \     \
   2    1
       /
     -1
'''
a=Node(10)
a.left=Node(5)
a.left.right=Node(2)
a.right=Node(5)
a.right.right=Node(1)
a.right.right.left=Node(-1)

class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
        
    def min_sum(self):
        if self.left and self.right:
            a,List1=self.left.min_sum()
            b,List2=self.right.min_sum()
            if a<b:
                a+=self.val
                List1.append(self.val)
                return a,List1
            else:
                b+=self.val
                List2.append(self.val)
                return b,List2
        elif self.left:
            a,List=self.left.min_sum()
            List.append(self.val)
            a+=self.val
            return a,List
        elif self.right:
            a,List=self.right.min_sum()
            List.append(self.val)
            a+=self.val
            return a,List
        else:
            List=[self.val]
            return self.val,List