'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given a singly linked list and an integer k, remove the kth last element from the list. 
k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.

Do this in constant space and in one pass.
'''

#List=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
k=5


class linked_list:
    def __init__(self,val=None,next_elem=None):
        self.val=val
        self.next_elem=next_elem
        
    
def remove_element(linked,k):
    i=-1
    a=linked
    b=linked
    while a.next_elem:
        i+=1
        a=a.next_elem
        if i>=k+1:
            b=b.next_elem
            
        
    b.next_elem=b.next_elem.next_elem
    return linked
    
   
linked=linked_list(val=0)
a=linked
for i in range(19):
    a.next_elem=linked_list(val=i+1)
    a=a.next_elem
    
    
bb=linked
for i in range(20):
    print(bb.val)
    if bb.next_elem:
        bb=bb.next_elem
        
        