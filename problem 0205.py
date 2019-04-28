'''
Good morning! Here's your coding interview problem for today.

This problem was asked by IBM.

Given an integer, find the next permutation of it in absolute order. 
For example, given 48975, the next permutation would be 49578.
'''

number = 48975

def next_permutation(number):
    nbr=str(number)
    lenn=len(nbr)
    
    result=True
    i=lenn-1
    while result==True:
        i=i-1

        if i==-1:
            print('no permutation')
            return number
        val=nbr[i]
        min_=-1
        for j in range(lenn-1,i,-1):

            if nbr[j]>val:
                result=False
                if min_==-1:
                    min=nbr[j]
                    pos=j
                else:
                    if nbr[j]<=min_:
                        
                        pos=j
                        min_=nbr[j]
                
                
    temp1=nbr[i]
    temp2=nbr[pos]
    nbr=nbr[:i]+temp2+nbr[i+1:pos]+temp1+nbr[pos+1:]
    List=[]
    for j in range(i+1,lenn):
        List.append(nbr[j])
    List.sort()
    
    nbr=nbr[:i+1]
    for j in range(lenn-i-1):
        nbr+=List[j]
    return int(nbr)
                