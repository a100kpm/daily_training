'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

On a mysterious island there are creatures known as Quxes which come in three colors: 
    red, green, and blue. One power of the Qux is that if two of them are standing 
    next to each other, they can transform into a single creature of the third color.

Given N Quxes standing in a line, determine the smallest number of them remaining 
after any possible sequence of such transformations.

For example, given the input ['R', 'G', 'B', 'G', 'B'], it is possible to end 
up with a single Qux through the following steps:

        Arrangement       |   Change
----------------------------------------
['R', 'G', 'B', 'G', 'B'] | (R, G) -> B
['B', 'B', 'G', 'B']      | (B, G) -> R
['B', 'R', 'B']           | (R, B) -> G
['B', 'G']                | (B, G) -> R
['R']                     |
'''


array = ['R', 'G', 'B', 'G', 'B']

def find_min(array,num=0):
    lenn=len(array)
    changement=[]
    for i in range(lenn-1):
        if array[i]!=array[i+1]:
            changement.append(i)
          

    lenn2=len(changement)
    if lenn2==0:
        return num
    rez=[]
    for i in changement:
        array_temp=array.copy()
        val1=array[i]
        val2=array[i+1]
        del(array_temp[i])
        array_temp[i]=transfo(val1,val2)
        rez.append(find_min(array_temp,num+1))
    if num!=0:
        return max(rez)
    return  lenn-max(rez)

def transfo(val1,val2):
    if val1==val2:
        print('error')
        return
    
    if 'R' in (val1,val2) and 'G' in (val1,val2):
        return 'B'
    if 'B' in (val1,val2) and 'G' in (val1,val2):
        return 'R'
    if 'B' in (val1,val2) and 'R' in (val1,val2):
        return 'G'
