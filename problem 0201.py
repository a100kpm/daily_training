'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

You are given an array of arrays of integers, where each array corresponds to a row in a triangle of numbers. 
For example, [[1], [2, 3], [1, 5, 1]] represents the triangle:

      1
     2 3
    1 5 1
   1 1 6 7
  99 1 1 1 1

We define a path in the triangle to start at the top and go down one row at a 
time to an adjacent value, eventually ending with an entry on the bottom row. For example, 1 -> 3 -> 5. The weight of the path is the sum of the entries.

Write a program that returns the weight of the maximum weight path.
'''
triangle1 = [[1], [2, 3], [1, 5, 1]]
triangle2 = [[1], [2, 3], [1, 5, 1], [1,1,6,7]]
triangle3 = [[1], [2, 3], [1, 5, 1], [1,1,6,7], [99,1,1,1,1]]

def find_max_path(triangle,step=0,pos=0):
    if step==0:
        return triangle[0][0]+find_max_path(triangle,1,0)
    lenn=len(triangle)-1
    if step<lenn:
        return max(triangle[step][pos]+find_max_path(triangle,step+1,pos),
                   triangle[step][pos+1]+find_max_path(triangle,step+1,pos+1)
                   )
    return max(triangle[step][pos],triangle[step][pos+1])