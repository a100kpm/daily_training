'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Implement a bit array.

A bit array is a space efficient array that holds a value of 1 or 0 at each index.

    init(size): initialize the array with size
    set(i, val): updates index at i with val where val is either 1 or 0.
    get(i): gets the value at index i.

'''

class space_array:
    def __init__(self,size):
        self.array=[0]*size
        
    def set_(self,i,val):
        self.array[i]=val
        
    def get(self,i):
        return self.array[i]
    
    
# =============================================================================
# =============================================================================
# =============================================================================
# =============================================================================
# # # #     NAY NAY NAY NAY
# # # # =============================================================================
# =============================================================================
# =============================================================================
# 
# =============================================================================
