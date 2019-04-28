'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given an array of integers where every integer occurs three times
 except for one integer, which only occurs once, find and return the non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.

Do this in O(N) time and O(1) space.
'''

# not my code, 
# also it seems to be the 'right' answer, even though it's a o(n log n) in disguise and not a o(n)
# =============================================================================
# la solution utilisant l'astuce des bits est techniquement en o(n log n) et pas o(n)
# =============================================================================
import math

L1 = [6, 1, 3, 3, 3, 6, 6]

L2 = [13, 19, 13, 13]

L = [1,3,3,3,5,5,5,7,7,7,9,9,9,11,11,11]

def find_unique(L):
    n=len(L)
    
    ones = 0
    twos = 0
    
    for i in range(n):
        twos = twos | (ones&L[i])
        
        ones = ones ^ L[i]
        
        common_bit_mask = ~(ones & twos)
        
        ones &= common_bit_mask
        
        twos &= common_bit_mask
        
    return ones
    
