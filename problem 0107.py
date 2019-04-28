'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

Print the nodes in a binary tree level-wise. For example, the following should print 1, 2, 3, 4, 5, 6, 7, 8.

      1
     / \
    2   3
   /   / \
  4   5   6
 / \
7   8
'''


class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
a=Node(1)
a.left=Node(2)
a.right=Node(3)
a.left.left=Node(4)
a.right.left=Node(5)
a.right.right=Node(6)
a.left.left.left=Node(7)
a.left.left.right=Node(8)

def show_tree(Tree):
    List=find_node_level(Tree)
    lenn=len(List)
    compteur=0
    lvl=0
    while compteur<lenn:
        for i in range(lenn):
            if List[i][1]==lvl:
                print(List[i][0])
                compteur+=1
        lvl+=1
    
def find_node_level(Tree,lvl=0):
    List=[]
    List.append([Tree.val,lvl])
    if Tree.left:
        List.extend(find_node_level(Tree.left,lvl+1))
    if Tree.right:
        List.extend(find_node_level(Tree.right,lvl+1))
    return List
    
    
