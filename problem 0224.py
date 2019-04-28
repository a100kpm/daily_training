'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Given a sorted array, find the smallest positive integer that is not the sum of a subset of the array.

For example, for the input [1, 2, 3, 10], you should return 7.

Do this in O(N) time.
'''

input_ = [1,2,3,10]


def smallest_not_in_sum(input_):
    lenn=len(input_)
    max_=0
    
    for i in range(lenn):
        if input_[i]<=max_+1:
            max_+=input_[i]
        else:
            return max_+1
    return max_+1
            
