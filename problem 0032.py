'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Jane Street.

Suppose you are given a table of currency exchange rates, represented as a 2D array. 
Determine whether there is a possible arbitrage: that is, 
whether there is some sequence of trades you can make, 
starting with some amount A of any currency, so that you can end up with 
some amount greater than A of that currency.

There are no transaction costs and you can trade fractional quantities.
'''


import numpy as np
import random

table_=np.zeros([12,12])

for i in range(12):
    for j in range(12):
        if i==j:
            table_[i,j]=1
        elif table_[j,i]==0:
            table_[i,j]=random.randrange(1,100)
        else:
            table_[i,j]=1./table_[j,i]
        
        
def search_unfair(table_):
    lenn=np.shape(table_)[0]
    
    for i in range(lenn):
        for j in range(lenn):
            if table_[i,j]*table_[j,i]>1:
                return True,i,j
    return False
