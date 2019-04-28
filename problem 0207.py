'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Dropbox.

Given an undirected graph G, check whether it is bipartite. 
Recall that a graph is bipartite if its vertices can be divided into two independent sets,
 U and V, such that no edge connects vertices of the same set.
'''

import numpy as np

graph = np.array([[0,1,1,1,0,0,0],
                  [1,0,0,0,0,0,0],
                  [1,0,1,1,0,0,0],
                  [1,0,1,1,0,0,0],
                  [0,0,0,0,0,1,1],
                  [0,0,0,0,1,0,1],
                  [0,0,0,0,1,1,0]
                  ])



def bipartite(graph):
    lenn=np.shape(graph)[0]
    list_=set()
    
    compteur=0
    while len(list_)<lenn:
        compteur+=1
        
        for i in range(lenn):
            if i not in list_:
                break
            
        current_list=[i]
        while len(current_list):
            for j in range(lenn):
                val = graph[current_list[0]][j]
                if val==1 and j not in list_ and j not in current_list:
                    list_.add(j)
                    current_list.append(j)
            current_list=current_list[1:]
            
    if compteur==2:
        return True
    return False
            
                    
        
    
    