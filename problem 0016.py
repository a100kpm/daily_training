'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Twitter.

You run an e-commerce website and want to record the last N order ids in a log. 
Implement a data structure to accomplish this, with the following API:

    record(order_id): adds the order_id to the log
    
    get_last(i): gets the ith last element from the log. 
    i is guaranteed to be smaller than or equal to N.

You should be as efficient with time and space as possible.
'''


log=None
N=10



class List_id:
    def __init__(self, val, Next=None):
        self.num = 1
        self.val = val
        self.next = Next
        self.long = N
        
        
    def record(order_id,log):
        if log==None:
            log=List_id(order_id)
        elif log.num == log.long:
            log=log.next
            logs=log
            for _ in range (log.long-1):
                log.num+=1
                log=log.next
            log.next=List_id(order_id)
        else:
            logs=log
            while logs.next:
                logs.num+=1
                logs=logs.next
        return log
                
                
            
            
                
            
        
        
        