'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Twitter.

Given a list of numbers, create an algorithm that arranges 
them in order to form the largest possible integer. For example, 
given [10, 7, 76, 415], you should return 77641510.
'''
import numpy as np


List=[10,7,76,415]


def re_order_list(List):
    lenn=len(List)
    keep_val=[]
#    order=['','9','8','7','6','5','4','3','2','1','0']
    length_max=0
    for i in range(lenn):
        string_=str(List[i])
        keep_val.append(string_)
        if len(string_)>length_max:
            length_max=len(string_)
     
    multiplicateur=0.1
    base_multiplicateur=10**(-length_max)
    for i in range(lenn):
        
        string_=keep_val[i]

        List[i]=List[i]/10**(len(string_)-1)*1.0

        val=[]
        for j in range(1,len(string_)):

            nbr=int(string_[j])-int(string_[j-1])
            val.append(nbr)
            
        List[i]=int(keep_val[i][0])
        for j in range(len(val)):
            List[i]+=base_multiplicateur*multiplicateur*(j+1)*nbr
            
    
    sort_index=np.argsort(List)
    
    result=''
    for i in range(lenn-1,-1,-1):
        result+=keep_val[sort_index[i]]
        
    return int(result)
        