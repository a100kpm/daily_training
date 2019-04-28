'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given the root of a binary search tree, and a target K, 
return two nodes in the tree whose sum equals K.

For example, given the following tree and K of 20

    10
   /   \
 5      15
       /  \
     11    15

Return the nodes 5 and 15.
'''

class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
a = Node(10)
a.left = Node(5)
a.right= Node(15)
a.right.right= Node(15)
a.right.left= Node(11)

k= 20
# =============================================================================
# =============================================================================
# #  marche dans un sub tree uniquement !!!!
# # def find_sum_in_tree(a,k,current_node):
# #     val1=None
# #     val3=None
# #     val2=None
# #     val4=None
# #     if k==0:
# #         return current_node
# #     
# #     if (not a.left) and (not a.right):
# #         if k==a.val:
# #             current_node.append(a)
# #             return current_node
# #         else:
# #             return None
# #         
# #     new_current_node=current_node.copy()
# #     new_current_node2=current_node.copy()
# #     new_current_node2.append(a)
# #     if a.left:
# #         val1=find_sum_in_tree(a.left,k,new_current_node)
# #         val2=None
# #         if k>=a.val:
# #             val2=find_sum_in_tree(a.left,k-a.val,new_current_node2)
# #             
# #     if a.right:
# #         val3=find_sum_in_tree(a.right,k,new_current_node)
# #         val4=None
# #         if k>=a.val:
# #             val4=find_sum_in_tree(a.right,k-a.val,new_current_node2)        
# #     
# #     if val1:
# #         return val1
# #     if val2:
# #         return val2
# #     if val3:
# #         return val3
# #     if val4:
# #         return val4
# #     
# # =============================================================================
# 
# =============================================================================
resultat=[]
import numpy as np

def find_all_node_and_value(Tree,resultat,result=1):
    resultat.append([Tree,Tree.val])
    if Tree.left:
        find_all_node_and_value(Tree.left,resultat,result=0)
    if Tree.right:
        find_all_node_and_value(Tree.right,resultat,result=0)
    if result==1:
        return resultat
    
def find_sum_in_tree(Tree,k):
    resultat=[]
    List_node = find_all_node_and_value(Tree,resultat)
    
    somme_node = sommeur_node(List_node,k,[])
    
    return somme_node

def sommeur_node(List_node,k,current_list):
    if k==0:
        return current_list
    
    if np.shape(List_node)==(2,):
        if k==List_node[0][1]:
            current_list.append(List_node[0])
            return current_list
        else:
            return None
        
        
    val1=None
    val2=None
    new_current_list=current_list.copy()
    val1=sommeur_node(List_node[1:],k,new_current_list)
    
    if k>=List_node[0][1]:
        new_current_list2=current_list.copy()
        new_current_list2.append(List_node[0])
        val2=sommeur_node(List_node[1:],k-List_node[0][1],new_current_list2)
        
    if val1:
        return val1
    if val2:
        return val2
    
    
    
    
    
    
    