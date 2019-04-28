'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Stripe.

Write a map implementation with a get function that lets you retrieve the value of a key at a particular time.

It should contain the following methods:

    set(key, value, time): sets key to value for t = time.
    get(key, time): gets the key at t = time.

The map should work like this. If we set a key at a particular time, 
it will maintain that value forever or until it gets set at a later time. 
In other words, when we get a key at a time, it should return the value that was 
set for that key set at the most recent time.

Consider the following examples:

d.set(1, 1, 0) # set key 1 to value 1 at time 0
d.set(1, 2, 2) # set key 1 to value 2 at time 2
d.get(1, 1) # get key 1 at time 1 should be 1
d.get(1, 3) # get key 1 at time 3 should be 2

d.set(1, 1, 5) # set key 1 to value 1 at time 5
d.get(1, 0) # get key 1 at time 0 should be null
d.get(1, 10) # get key 1 at time 10 should be 1

d.set(1, 1, 0) # set key 1 to value 1 at time 0
d.set(1, 2, 0) # set key 1 to value 2 at time 0
d.get(1, 0) # get key 1 at time 0 should be 2
'''
import numpy as np

class mapp:
    def __init__(self,key=None,value=None,time=None):
        
        self.key=[key]
        self.value=[value]
        self.time=[time]
        
        
    def sett(self,key,value,time):
        if key in self.key:
            finder=[i for i,val in enumerate(self.key) if val==key]
            lenn=len(finder)
            Lister_time=[]
            for i in range(lenn):
                Lister_time.append(self.time[finder[i]])
                
            if time in Lister_time:
                a=Lister_time.index(time)
                b=finder[a]
                self.value[b]=value
                
            else:
                self.key.append(key)
                self.value.append(value)
                self.time.append(time)
            
        else:
            self.key.append(key)
            self.value.append(value)
            self.time.append(time)
        
    def gett(self,key,time):
        
        finder=[i for i,val in enumerate(self.key) if val==key]
        lenn=len(finder)
        Lister_time=[]
        for i in range(lenn):
            Lister_time.append(self.time[finder[i]])
        
        order_time = np.sort(Lister_time)
        compteur=None
        for i in range(lenn-1,-1,-1):
            if order_time[i]<=time:
                compteur=order_time[i]
                break
        
        if compteur==None:
            print("No value")
            return None
        
        a=Lister_time.index(compteur)
        b=finder[a]
        
        print('value',self.value[b])
        return self.value[b]
        
        
        
        