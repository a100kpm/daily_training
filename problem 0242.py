'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Twitter.

You are given an array of length 24, where each element represents the number of 
new subscribers during the corresponding hour. Implement a data structure that efficiently supports the following:

    update(hour: int, value: int): Increment the element at index hour by value.
    query(start: int, end: int): Retrieve the number of subscribers that have signed up between start and end (inclusive).

You can assume that all values get cleared at the end of the day, and that you will 
not be asked for start and end values that wrap around midnight.
'''


import random

List=[]

for i in range(24):
    List.append(random.randrange(0,100))


class subscriber:
    def __init__(self):
        self.sub=[0]*24
        
    def update(self,hour, value):
        self.sub[hour]+=value
        
    def query(self,start,end):
        return sum(self.sub[start:end])
        
    
a = subscriber()
for i in range(24):
    a.update(i,List[i])
    
print(a.query(1,3))
print(a.query(6,5))
print(a.sub)