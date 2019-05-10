'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Pandora.

Given an undirected graph, determine if it contains a cycle.
'''


graph=[ [1,2],
        [0,3],
        [0,4],
        [1,5],
        [2,6],
        [3],
        [4,7,8],
        [6],
        [6]
        ]
# we are assuming that the graph isn't disjointed
# (else we would need to use that function on all of it's sub-parts)

def is_cycle(graph,start=0):
    List_visited=[start]
    List_to_visit=[]
    for i in graph[start]:
        List_to_visit.append(i)    
    
    if len(List_to_visit)==0:
        return False
    
    search=True
    while search==True:
        val=List_to_visit.pop(0)
        print(val)
        if val in List_to_visit:
            return True
        List_visited.append(val)
        for i in graph[val]:
            if i not in List_visited:
                List_to_visit.append(i)
                
        if len(List_to_visit)==0:
            search=False
            
    return False
        
