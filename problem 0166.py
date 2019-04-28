'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Uber.

Implement a 2D iterator class. It will be initialized with an array of arrays, and should implement the following methods:

    next(): returns the next element in the array of arrays. If there are no more elements, raise an exception.
    has_next(): returns whether or not the iterator still has elements left.

For example, given the input [[1, 2], [3], [], [4, 5, 6]], calling next() repeatedly should output 1, 2, 3, 4, 5, 6.

Do not use flatten or otherwise clone the arrays. Some of the arrays can be empty.
'''

class dd_iterator():
    def __init__(self,elem=[]):
        self.val=[elem]
        self.current=[0,-1]
        self.max_current=1
        
    def add_elem(self,elem):
        self.val.append(elem)
        self.max_current+=1
        
    def next_(self):
        val,pos1,pos2=self.has_next(all_=1)
        if val==True:
            self.current=[pos1,pos2]
            return self.val[pos1][pos2]
        else:
            print('no next element')
        
    def has_next_aux(self):
        val1=self.current[0]
        val2=self.current[1]
        try:
            if self.val[val1][val2+1]:
                return True,val1,val2+1
        except:
            val1+=1
            val2=0
        while val1<self.max_current:
            try:
                if self.val[val1][val2]:
                    return True,val1,val2
            except:
                val1+=1
        return False,0,0
    
    def has_next(self,all_=0):
        val,pos1,pos2=self.has_next_aux()
        if all_==0:
            
            return val
        if all_==1:
            return val,pos1,pos2
        
        
a=dd_iterator([1,2])
a.add_elem([3])
a.add_elem([])
a.add_elem([4,5,6])
        
        