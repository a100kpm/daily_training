'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Goldman Sachs.

Given a list of numbers L, implement a method sum(i, j) 
which returns the sum from the sublist L[i:j] (including i, excluding j).

For example, given L = [1, 2, 3, 4, 5], sum(1, 3) should return sum([2, 3]), which is 5.

You can assume that you can do some pre-processing. sum() should be optimized over the pre-processing step.
'''

L = [1,2,3,4,5]



class pre_pro_list():
    def __init__(self,L=None):
        if L==None:
            self.List=[]
        else:
            self.List=L
        self.prepro_List=None
        
    def preprocess_list(self):
        self.prepro_List=[]
        self.prepro_List.append(self.List[0])
        lenn=len(self.List)
        for i in range(1,lenn):
            self.prepro_List.append(self.List[i]+self.prepro_List[-1])
            
    def sum(self,i,j):
        if self.prepro_List==None:
            self.preprocess_list()
        lenn=len(self.List)
        if i<=j and i>=0 and j<=lenn:
            if i==0:
                return self.prepro_List[j-1]
            if i==j:
                return 0
            return self.prepro_List[j-1]-self.prepro_List[i-1]
            
    