'''
Good morning! Here's your coding interview problem for today.

This problem was asked by LinkedIn.

A wall consists of several rows of bricks of various integer lengths and uniform height. 
Your goal is to find a vertical line going from the top to the bottom of the wall 
that cuts through the fewest number of bricks. If the line goes through the edge between two bricks, 
this does not count as a cut.

For example, suppose the input is as follows, where values in each row 
represent the lengths of bricks in that row:

[[3, 5, 1, 1],
 [2, 3, 3, 2],
 [5, 5],
 [4, 4, 2],
 [1, 3, 3, 3],
 [1, 1, 6, 1, 1]]

The best we can we do here is to draw a line after the eighth brick, 
which will only require cutting through the bricks in the third and fifth row.

Given an input consisting of brick lengths for each row such as the one above, 
return the fewest number of bricks that must be cut to create a vertical line.
'''

wall = [    [3, 5, 1, 1],
             [2, 3, 3, 2],
             [5, 5],
             [4, 4, 2],
             [1, 3, 3, 3],
             [1, 1, 6, 1, 1]
        ]

def pre_proc_wall(wall):
    for i in wall:
        prec=0
        for j in range(len(i)):
            i[j]+=prec
            prec=i[j]
            
    return wall,max([max(x) for x in wall])

def cut_brick(wall):
    wall,val_max=pre_proc_wall(wall)
    
    result=[0]*(val_max-1)
    
    for i in range(1,val_max):
        nbr=0
        for j in wall:
            if i not in j:
                nbr+=1
        result[i-1]=nbr
        
    return result.index(min(result))+1
    