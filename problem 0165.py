'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given an array of integers, return a new array where each element in the new array
 is the number of smaller elements to the right of that element in the original input array.

For example, given the array [3, 4, 9, 6, 1], return [1, 1, 2, 1, 0], since:

    There is 1 smaller element to the right of 3
    There is 1 smaller element to the right of 4
    There are 2 smaller elements to the right of 9
    There is 1 smaller element to the right of 6
    There are no smaller elements to the right of 1
'''

List = [3,4,9,6,1]

def smaller_in_list(List):
    lenn=len(List)
    List_=[]
    for i in range(lenn):
        compteur=0
        for j in range(i+1,lenn):
            if List[j]<List[i]:
                compteur+=1
        List_.append(compteur)
        
    return List_