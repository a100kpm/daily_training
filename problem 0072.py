'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

In a directed graph, each node is assigned an uppercase letter. We define a path's 
value as the number of most frequently-occurring letter along that path. For example, 
if a path in the graph goes through "ABACA", the value of the path is 3, 
since there are 3 occurrences of 'A' on the path.

Given a graph with n nodes and m directed edges, return the largest value path of the graph.
 If the largest value is infinite, then return null.

The graph is represented with a string and an edge list. 
The i-th character represents the uppercase letter of the i-th node. 
Each tuple in the edge list (i, j) means there is a directed edge from the i-th node to the j-th node. 
Self-edges are possible, as well as multi-edges.

For example, the following input graph:

ABACA

[(0, 1),
 (0, 2),
 (2, 3),
 (3, 4)]

Would have maximum value 3 using the path of vertices [0, 2, 3, 4], (A, A, C, A).

The following input graph:

A

[(0, 0)]

Should return null, since we have an infinite loop.
'''

graph = 'ABACA'

graph2=[(0,1),
        (0,2),
        (2,3),
        (3,4),]




def all_path(graph,graph2,start=0,iteration=-1,max_iter=4,embrenchement=0):
    iteration+=1
    a=[]
    if iteration > max_iter:
        return None
    possible=False
    which=[]
    for i in range(len(graph2)):
        if graph2[i][0]==start:
            possible=True
            which.append(i)
    if possible==True:
        if len(which)>1:
            n_embrenchement=0
        else:
            n_embrenchement=embrenchement+1
        for i in range(len(which)):
            a.extend([start, all_path(graph,graph2,start=graph2[which[i]][1],iteration=iteration,max_iter=max_iter,embrenchement=n_embrenchement)] )
    if possible==False:
        a.extend([start])
        a.extend(['fin'])
        a.extend([embrenchement+1])
        
    return a

def read_allpath(list_path):
    read_path=[]

    j=0
    i=0
    list_path=str(list_path)
    lenn=len(list_path)
    while j<lenn:
        j+=1
        if list_path[i]=='[' or list_path[i]==']':
            list_path=list_path[:i]+list_path[i+1:]
        else:
            i+=1
    
    nbr_path=0
    list_path=list_path.split(',')
    for i in range(len(list_path)):
        if list_path[i]==" 'fin'":
            nbr_path+=1
    
    j=0
    courant=[]
    i=-1
    while j<nbr_path:
        i+=1
        if list_path[i]==" 'fin'":
            read_path.append(courant)
            i+=1
            enleve=int(list_path[i])+1
            courant=courant[:-enleve]
            j+=1
        else:
            courant.append(int(list_path[i]))
            
    return read_path
        

def infinite(list_path):
    a=str(list_path)
    if "None" in a:
        return True
    return False
# si ya un none return true else return false
    
def definition_score(path,graph):
    noteur=[]
    for i in range(len(graph)):
        if [graph[i],0] in noteur:
            pass
        else:
            noteur.append([graph[i],0])
    lenn=len(noteur)
    val_list=[]
    for i in range(len(path)):
        compteur_lettre=[0]*lenn
        for j in range(len(path[i])):
            lettre = graph[path[i][j]]
            kk=-1
            for k in noteur:
                kk+=1
                if k[0]==lettre:
                    compteur_lettre[kk]+=1
        val_list.append(max(compteur_lettre))
    return max(val_list)
        
# donne le score max

def highest(graph,graph2):
    list_path=all_path(graph,graph2)
    if infinite(list_path):
        return None
    read_path=read_allpath(list_path)

    return definition_score(read_path,graph)
    














        
        
        
        
        
        
        
        
        
        
        
        
        
        