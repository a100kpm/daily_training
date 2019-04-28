'''
Good morning! Here's your coding interview problem for today.

Given a 2-D matrix representing an image, a location of a pixel in the screen and a color C,
 replace the color of the given pixel and all adjacent same colored pixels with C.

For example, given the following matrix, and location pixel of (2, 2), and 'G' for green:

B B W
W W W
W W W
B B B

Becomes

B B G
G G G
G G G
B B B
'''

import numpy as np

array=np.array([['B','B','W'],['W','W','W'],['W','W','W'],['B','B','B']])


def paint_color(array,pos,color):
    lenn=np.shape(array)[0]
    lenn2=np.shape(array)[1]
    zone_color=array[pos[0]][pos[1]]
    if zone_color==color:
        return
    
    array[pos[0]][pos[1]]=color
    
    if pos[0]<lenn-1 and array[pos[0]+1][pos[1]]==zone_color:
        paint_color(array,[pos[0]+1,pos[1]],color)
    if pos[1]<lenn2-1 and array[pos[0]][pos[1]+1]==zone_color:
        paint_color(array,[pos[0],pos[1]+1],color)
    if pos[0]>0 and array[pos[0]-1][pos[1]]==zone_color:
        paint_color(array,[pos[0]-1,pos[1]],color)
    if pos[1]>0 and array[pos[0]][pos[1]-1]==zone_color:
        paint_color(array,[pos[0],pos[1]-1],color)
    
    
    
    