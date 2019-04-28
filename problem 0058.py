'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

An sorted array of integers was rotated an unknown number of times.

Given such an array, find the index of the element in the array in faster 
than linear time. If the element doesn't exist in the array, return null.

For example, given the array [13, 18, 25, 2, 8, 10] and the element 8, 
return 4 (the index of 8 in the array).

You can assume all the integers in the array are unique.
'''


List = [13,18,25,2,8,10]
elem = 8
lennn=len(List)-1

def find_elem(List,elem,debut=0,fin=lennn):

    middle=int((lennn+1+debut)/2+((lennn+3+debut)%2)-1)
    print(debut)
    print(middle)
    print(fin)
    input()   
    
    
    a=List[debut]
    b=List[middle]
    c=List[fin]
    
    if a==elem:
        return debut
    if b==elem:
        return middle
    if c==elem:
        return fin
    
    if a<=b and a<=elem and b>=elem:
        return find_elem(List,elem,debut=debut,fin=middle)
    elif b<=c and b<=elem and c>=elem:
        return find_elem(List,elem,debut=middle,fin=fin)
    elif a>=b and b<c:
        return find_elem(List,elem,debut=debut,fin=middle)
    else:
        return find_elem(List,elem,debut=middle,fin=fin)