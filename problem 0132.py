'''
Good morning! Here's your coding interview problem for today.

This question was asked by Riot Games.

Design and implement a HitCounter class that keeps track of requests (or hits). 
It should support the following operations:

    record(timestamp): records a hit that happened at timestamp
    total(): returns the total number of hits recorded
    range(lower, upper): returns the number of hits that occurred between timestamps lower and upper (inclusive)

Follow-up: What if our system has limited memory?
'''

class HitCounter:
    def __init__(self):
        self.record=[]
        
    
    def total(self):
        return len(self.record)
    
    def recording(self,timestamp):
        self.record.append(timestamp)
        
    def range(self,lower,upper):
        compteur=0
        for i in range(len(self.record)):
            if self.record[i]<=upper and self.record[i]>=lower:
                compteur+=1
        return compteur