'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given the head of a singly linked list, swap every two nodes and return its head.

For example, given 1 -> 2 -> 3 -> 4, return 2 -> 1 -> 4 -> 3.
'''

class singly_list:
    def __init__(self,val):
        self.val=val
        self.next=None
        
    def add(self,val):
        if self.next:
            self.next.add(val)
        else:
            self.next=singly_list(val)
        

a=singly_list(1)
a.add(2)
a.add(3)
a.add(4)
a.add(5)



def pair_swaper(singly_list):
    if singly_list.next:
        a=singly_list.val
        singly_list.val=singly_list.next.val
        singly_list.next.val=a
    if singly_list.next:
        if singly_list.next.next:
            pair_swaper(singly_list.next.next)
        