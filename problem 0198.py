'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given a set of distinct positive integers, find the largest subset such that every pair 
of elements in the subset (i, j) satisfies either i % j = 0 or j % i = 0.

For example, given the set [3, 5, 10, 20, 21], you should return [5, 10, 20]. 
Given [1, 3, 6, 24], return [1, 3, 6, 24].
'''

set_1 = [3,5,10,20,21]
set_2 = [1,3,6,24]

def find_max_modulo_subset(set_,current=[]):
    if len(set_)==0:
        return len(current),current
    
    current1=current.copy()
    current2=current.copy()
    current2.append(set_[0])
    
    lenn=len(current)
    choice=1
    for i in range(lenn):
        if set_[0]%current[i]==0 or current[i]%set_[0]==0:
            pass
        else:
            choice=0
            break
    a=0
    c=0    
    a,b=find_max_modulo_subset(set_[1:],current1)
    if choice==1:
        c,d=find_max_modulo_subset(set_[1:],current2)

    if c>a:
        return c,d
    return a,b
