'''
Good morning! Here's your coding interview problem for today.

This problem was asked by VMware.

The skyline of a city is composed of several buildings of various widths and heights, possibly
 overlapping one another when viewed from a distance. We can represent the buildings using 
 an array of (left, right, height) tuples, which tell us where on an imaginary x-axis a building 
 begins and ends, and how tall it is. The skyline itself can be described by a list of (x, height) tuples,
 giving the locations at which the height visible to a distant observer changes, and each new height.

Given an array of buildings as described above, create a function that returns the skyline.

For example, suppose the input consists of the buildings [(0, 15, 3), (4, 11, 5), (19, 23, 4)].
 In aggregate, these buildings would create a skyline that looks like the one below.

     ______  
    |      |        ___
 ___|      |___    |   | 
|   |   B  |   |   | C |
| A |      | A |   |   |
|   |      |   |   |   |
------------------------

As a result, your function should return [(0, 3), (4, 5), (11, 3), (15, 0), (19, 4), (23, 0)].
'''


array=[(0, 15, 3), (4, 11, 5), (19, 23, 4)]

def skyline(array):
#    supposing array is sorted by "start"
    end=array[-1][1]
    List_rez=[]
    pos_start=0
    i=0
    curr_val=0
    for k,l,m in array:
        if k==0 and l>0:
            curr_val=max(m,curr_val)
    while i<end:
        i+=1
        curr_max=0
        for k,l,m in array:
            if k<=i and l>i:
                curr_max=max(m,curr_max)
            
        if curr_max!=curr_val:
            List_rez.append((pos_start,curr_val))
            pos_start=i
            curr_val=curr_max
            
    List_rez.append((end,0))
    return List_rez
        
    