'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

You are in an infinite 2D grid where you can move in any of the 8 directions:

 (x,y) to
    (x+1, y),
    (x - 1, y),
    (x, y+1),
    (x, y-1),
    (x-1, y-1),
    (x+1,y+1),
    (x-1,y+1),
    (x+1,y-1)

You are given a sequence of points and the order in which you need to cover the points. 
Give the minimum number of steps in which you can achieve it. You start from the first point.

Example:

Input: [(0, 0), (1, 1), (1, 2)]
Output: 2

It takes 1 step to move from (0, 0) to (1, 1). It takes one more step to move from (1, 1) to (1, 2).
'''

List = [(0, 0), (1, 1), (1, 2)]

def nbr_step(List):
    compteur=0
    lenn=len(List)-1
    for i in range(lenn):
        compteur+=cout_distance(List[i],List[i+1])
        
    return compteur

def cout_distance(pos1,pos2):
    a = abs(pos1[0]-pos2[0])
    b = abs(pos1[1]-pos2[1])
    return max(a,b)