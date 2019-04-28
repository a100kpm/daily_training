'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

The power set of a set is the set of all its subsets. Write a function that, 
given a set, generates its power set.

For example, given the set {1, 2, 3}, it should return 
{{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

You may also use a list or array to represent a set.
'''

set_=[1,2,3]

def power_set(set_):
    lenn=len(set_)
    result=[]
    nbr=2**lenn
    for i in range(nbr):
        g=nbr_to_bi(i,lenn)
        List_=[]
        for j in range(len(g)):
            if g[j]==1:
                List_.append(set_[j])
        result.append(List_)
        
    return result

def nbr_to_bi(i,lenn):
    result=[]
    for _ in range(lenn):
        result.append(0)
    for j in range(lenn):
        if i%2==1:
            result[j]=1
            i=i-1
        i=i/2
    return result
    
    


# SO UGLY TO DO IT IN ITERATIVE INSTEAD OF RECURSIVE!!!!!