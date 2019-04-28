'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Nvidia.

You are given a list of N points (x1, y1), (x2, y2), ..., (xN, yN) representing a polygon.
 You can assume these points are given in order; that is, you can construct the polygon by
 connecting point 1 to point 2, point 2 to point 3, and so on, finally looping around to connect point N to point 1.

Determine if a new point p lies inside this polygon.
 (If p is on the boundary of the polygon, you should return False).
'''


# =============================================================================
# =============================================================================
# # solution:
# #     tracer une ligne horizontal (vers la droite ou la gauche, mais pas les deux) partant du point de départ
# #     et compter le nombre de côté traversé
# #     Si le nombre de côté traversé est impair --> a l'intérieur, sinon a l'extérieur
# =============================================================================
# =============================================================================

# on peut techniquement rajouter une détection de l'appartenance au bord (produit vectoriel)

List_point = [(0,0),(5,0),(3,3)]
point=(2,0)

def cut(position,point1,point2):
    if point1[0]>position[0] and point2[0]>position[0]:
        print('cas1')
        if min(point1[1],point2[1])<position[1] and max(point1[1],point2[1]>position[1]):
            
            return True
        else:
            return False
        
    elif point1[0]<position[0] and point2[0]<position[0]:
        print('cas2')
        return False
    
    else:
        print('cas3')
        vector=[point2[0]-point1[0],point2[1]-point1[1]]
        hauteur=abs(point1[1]-position[1])
        if vector[1]==0:
            return False
        factor=abs(hauteur/vector[1])
        
        if (point1[0]+factor*vector[0])>position[0]:
            return True
        else:
            return False
        
    print('problem if arriving there!')
    

def inside(point,List_point):
    lenn=len(List_point)-1
    compteur=0
    for i in range(lenn):
        if cut(point,List_point[i],List_point[i+1])==True:
            compteur+=1
            
    if compteur%2==1:
        print('inside')
    else:
        print('outside')
