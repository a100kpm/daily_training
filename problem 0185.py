'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given two rectangles on a 2D graph, return the area of their intersection. If the rectangles don't intersect, return 0.

For example, given the following rectangles:

{
    "top_left": (1, 4),
    "dimensions": (3, 3) # width, height
}

and

{
    "top_left": (0, 5),
    "dimensions" (4, 3) # width, height
}

return 6.
'''


rec1 = {
    "top_left": (1, 4),
    "dimensions": (3, 3)
}

rec2 = {
    "top_left": (0, 5),
    "dimensions": (4, 3)
}


def intersect(rec1,rec2):
    corner_1 = rec1['top_left']
    corner_2 = rec2['top_left']
    
    size_1 = rec1['dimensions']
    size_2 = rec2['dimensions']
    
    all_border1=[]
    all_border2=[]
    
    all_border1.append(corner_1[1])
    all_border1.append(corner_1[1]-size_1[1])
    all_border1.append(corner_1[0])
    all_border1.append(corner_1[0]+size_1[0])
    
    all_border2.append(corner_2[1])
    all_border2.append(corner_2[1]-size_2[1])
    all_border2.append(corner_2[0])
    all_border2.append(corner_2[0]+size_2[0])
    
    new_border=[]
    new_border.append(min(all_border1[0],all_border2[0]))
    new_border.append(max(all_border1[1],all_border2[1]))
    new_border.append(max(all_border1[2],all_border2[2]))
    new_border.append(min(all_border1[3],all_border2[3]))
    
    hauteur=max(0,new_border[0]-new_border[1])
    largeur=max(0,new_border[3]-new_border[2])
    
    return hauteur*largeur