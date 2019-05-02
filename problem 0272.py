'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Spotify.

Write a function, throw_dice(N, faces, total), that determines how many ways it 
is possible to throw N dice with some number of faces each to get a specific total.

For example, throw_dice(3, 6, 7) should equal 15.
'''


def throw_dice(N,faces,total):
    if total<=0:
        return 0
    if N==1:
        if total<=faces:
            return 1
        else:
            return 0

    
    rez=0
    
    for i in range(1,faces+1):
        rez+=throw_dice(N-1,faces,total-i)
        
    return rez


def throw(N,faces,total):
    if N<=0:
        return 0
    return throw_dice(N,faces,total)


