'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Oracle.

We say a number is sparse if there are no adjacent ones in its binary representation. 
For example, 21 (10101) is sparse, but 22 (10110) is not. For a given input N, find the smallest sparse number greater than or equal to N.

Do this in faster than O(N log N) time.
'''


def next_not_sparse(number):
    if is_sparse(number):
        return number
    if is_sparse(number+1):
        return number+1
    if is_sparse(number+2):
        return number+2
    if is_sparse(number+3):
        return number+3
    
    print('error')
    return None



def is_sparse(number):
    number=bin(number)
    lenn=len(number)
    prev=1
    for i in range(3,lenn):
        if number[i]=='1' and prev==1:
            return False
        elif number[i]=='1':
            prev=1
        else:
            prev=0
    return True

    
def next_sparse(number):
    a=bin(number)
    print(a)
    next_=False
    
    a=a[0:2]+'0'+a[2:]
    lenn=len(a)
    while next_==False:
        prev=a[lenn-1]
        search=0
        for i in range(lenn-2,1,-1):
            if prev=='1' and a[i]=='1':
                pos=i-1
                search=1
                break
            else:
                prev=a[i]
        
        if search==0:
            next_=True
        else:
            while a[pos]=='1':
                pos=pos-1
            a=a[:pos]+'1'
            
            for i in range(pos+1,lenn):
                a+='0'
    print(a)
    return int(a,2)
                