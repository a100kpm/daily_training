'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

Compute the running median of a sequence of numbers. That is, given a stream of numbers, 
print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two middle numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

2
1.5
2
3.5
2
2
2
'''

import numpy as np

List=[2, 1, 5, 7, 2, 0, 5]

def median_stream(List):
    current_elem=[]
    parity = True
    
    lenn = len(List)
    middle=-1
    for i in range(lenn):
        parity=not(parity)
        current_elem.append(List[i])
        current_elem=np.sort(current_elem)
        current_elem=current_elem.tolist()
        if parity==False:
            middle+=1
            print(current_elem[middle])
        else:
            print((current_elem[middle]+current_elem[middle+1])/2)
            
        
        

            