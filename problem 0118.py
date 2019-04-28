'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given a sorted list of integers, square the elements and give the output in sorted order.

For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].
'''

List = [-9, -2, 0, 2, 3]

def sort_squared(List):
    lenn=len(List)
    
    if List[0]<0:
        new_List=[]
        positif=lenn
        for i in range(lenn):
            if List[i]>=0:
                positif=i
                break
        
        compteur=0
        negatif=positif-1
        while compteur<lenn:
            compteur+=1
            if positif==lenn:
                new_List.append(List[negatif]**2)
                negatif-=1
            elif negatif==-1:
                new_List.append(List[positif]**2)
                positif+=1
            elif List[positif]**2<List[negatif]**2:
                new_List.append(List[positif]**2)
                positif+=1
            else:
                new_List.append(List[negatif]**2)
                negatif-=1
            
    
    else:
        new_List= [x**2 for x in List]
    return new_List