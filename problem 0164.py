'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

You are given an array of length n + 1 whose elements belong to the set {1, 2, ..., n}. 
By the pigeonhole principle, there must be a duplicate. Find it in linear time and space.
'''


List = [1,3,4,5,7,8,5,2,2,6,6,2]

def find_duplicate(List):
    set_=set()
    lenn=len(List)
    List_duplicate=set()
    for i in range(lenn):
        if List[i] not in set_:
            set_.add(List[i])
        else:
            List_duplicate.add(List[i])
            
    return List_duplicate