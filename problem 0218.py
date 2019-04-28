'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Yahoo.

Write an algorithm that computes the reversal of a directed graph. 
For example, if a graph consists of A -> B -> C, it should become A <- B <- C.
'''

class Node:
    def __init__(self,val):
        self.val=val
        
    def __repr__(self):
        return str(self.val)
    
    def __eq__(self,other):
        return self.val == other.val
    
    def __hash__(self):
        return hash(self.val)
        

class Edge:
    def __init__(self,debut,fin):
        self.debut = debut
        self.fin = fin
        
    def __repr__(self):
        return "{}-->{}".format(self.debut,self.fin)
        

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = set()
        
    def add_node(self,node):
        if node in self.nodes:
            return
        self.nodes.add(node)
        
    def add_edge(self,debut,fin):
        self.edges.add(Edge(debut,fin))
        
    def get_edge(self):
        return self.edges
    
    def reverse_edge(self):
        for i in self.edges:
            a=i.debut
            i.debut=i.fin
            i.fin=a
            
    def reverse_edge2(self):
        self.edges = [Edge(i.fin,i.debut) for i in self.edges]
        
    def ruissellement(self,node):
        print(node)
        List_node=[]
        if type(node)!=list:
            node=[node]
#        lenn=len(node)
        for i in node:
            for j in self.edges:
                if j.debut==i:
                    List_node.append(j.fin)
        for k in range(len(List_node)):
            self.ruissellement(List_node[k])
    
    
    
g=Graph()
a=Node('a')
b=Node('b')
c=Node('c')
d=Node('d')


g.add_node(a)
g.add_node(b)
g.add_node(c)
g.add_edge(d,a)
g.add_edge(a,b)
g.add_edge(b,c)
edges=g.get_edge()
print(edges)
g.ruissellement(d)
g.ruissellement(b)
g.reverse_edge2()
edges=g.get_edge()
print(edges)
g.ruissellement(d)
g.ruissellement(b)

