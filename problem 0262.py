'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Mozilla.

A bridge in a connected (undirected) graph is an edge that, 
if removed, causes the graph to become disconnected. Find all the bridges in a graph.
'''

import numpy as np

graph1=np.array([
                [0,1,1,0,0],
                [1,0,0,0,0],
                [1,0,0,1,0],
                [0,0,1,0,1],
                [0,0,0,1,0]
                ])

graph2=np.array([
                [0,1,1,0,0],
                [1,0,0,1,0],
                [1,0,0,1,0],
                [0,1,1,0,1],
                [0,0,0,1,0]
                ])


def splash(graph,node_removed,node=0):
    lenn=np.shape(graph)[0]
    
    node_removed.append(node)
    for i in range(lenn):
        if i in node_removed:
            pass
        else:
            if graph[node][i]==1:
                node_removed=splash(graph,node_removed,i)
                
    return node_removed
    


def find_bridge(graph):
    bridge=[]
    
    lenn=np.shape(graph)[0]
    
    if len(splash(graph,[0],lenn-1))<lenn:
        bridge.append(0)
    for i in range(1,lenn):
        if len(splash(graph,[i]))<lenn:
            bridge.append(i)
            
    return bridge


print(find_bridge(graph1))
print(find_bridge(graph2))