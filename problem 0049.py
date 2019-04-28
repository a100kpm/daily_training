'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137,
since we would take elements 42, 14, -5, and 86.

Given the array [-5, -1, -8, -9], the maximum sum would be 0, 
since we would not take any elements.

Do this in O(N) time.
'''

List1=[34, -50, 42, 14, -5, 86]
List2=[-5, -1, -8, -9]

def find_max_contiguous(List):
    lenn=len(List)
    maxi = 0
    for i in range(1,lenn):
        List[i]=max(List[i],List[i]+List[i-1])
        if List[i]>maxi:
            maxi=List[i]
    
    return maxi