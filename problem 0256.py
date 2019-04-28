'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Fitbit.

Given a linked list, rearrange the node values such that they appear 
in alternating low -> high -> low -> high ... form.
 For example, given 1 -> 2 -> 3 -> 4 -> 5, you should return 1 -> 3 -> 2 -> 5 -> 4.
'''

class Linked_List():
    def __init__(self,val):
        self.val=val
        self.next=None
        
    def __repr__(self):
        result = "["
        node=self
        while node.next!=None:
            result+=str(node.val)
            result+=","
            node=node.next
        result+=str(node.val)
        result+="]"
            
        return result
        
a=Linked_List(1)
b=Linked_List(2)
c=Linked_List(3)
d=Linked_List(4)
e=Linked_List(5)

a.next=b
b.next=c
c.next=d
d.next=e

def low_high(Linked):
    a=Linked
    b=Linked.next
    low=True
    while a and b !=None:
        val1=a.val
        val2=b.val
        
        if low==True:
            low=False
            if val2<val1:
                c=a.val
                a.val=b.val
                b.val=c
        elif low==False:
            low=True
            if val1<val2:
                c=a.val
                a.val=b.val
                b.val=c
        a=a.next
        b=b.next

print(a)
low_high(a)
print(a)

