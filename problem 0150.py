'''
Good morning! Here's your coding interview problem for today.

This problem was asked by LinkedIn.

Given a list of points, a central point, and an integer k, find the nearest k points from the central point.

For example, given the list of points [(0, 0), (5, 4), (3, 1)], the central point (1, 2), and k = 2, return [(0, 0), (3, 1)].
'''

List_point = [(0, 0), (5, 4), (3, 1)]


def closest_to_central(central_point,k,List_point):
    List=[]
    lenn=len(List_point)
    
    for i in range(lenn):
        List.append(distance(central_point,List_point[i]))
        
    List_result=[]
    List_score=[]
    for i in range(k):
        List_result.append(List_point[i])
        List_score.append(List[i])
        
    max_=max(x for x in List_score)
    pos_max=List_score.index(max_)
    
    for i in range(k,lenn):
        if List[i]<max_:
            List_score[pos_max]=List[i]
            List_result[pos_max]=List_point[k]
            
            max_=max(x for x in List_score)
            pos_max=List_score.index(max_)
            
    return List_result

def distance(a,b):
    return ( (a[0]-b[0])**2+(a[1]-b[1])**2 )