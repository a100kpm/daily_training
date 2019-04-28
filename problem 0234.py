'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

Recall that the minimum spanning tree is the subset of edges of a tree that 
connect all its vertices with the smallest possible total edge weight. 
Given an undirected graph with weighted edges, compute the maximum weight spanning tree.
'''


# faire algo du smallest, mais en opposant les valeurs des edges


# sort les poids des edges par ordre croissant
# prendre le moins lourd et l'add sauf s'il cré un cycle
# repeat jusqu'a avoir V-1 edge ou V est le nombre de vertice (point)