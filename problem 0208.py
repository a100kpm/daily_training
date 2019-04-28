'''
Good morning! Here's your coding interview problem for today.

This problem was asked by LinkedIn.

Given a linked list of numbers and a pivot k, partition the linked list so that 
all nodes less than k come before nodes greater than or equal to k.

For example, given the linked list 5 -> 1 -> 8 -> 0 -> 3 and k = 3, 
the solution could be 1 -> 0 -> 5 -> 8 -> 3.
'''


class linked_list():
    def __init__(self,val):
        self.val=val
        self.next=None
        
    def add_val(self,val):
        a=self
        while a.next:
            a=a.next
        a.next=linked_list(val)
        
    def __str__(self):
        string = '['
        node=self
        while node.next:
            
            string += "{} ->".format(node.val)
            node=node.next
#            string += ', '
        string += "{}".format(node.val)
        string += ']'
        return string
    
    def pivot(self,pivo_val):
        a=self
        b=self
        while b:
            if b.val<=pivo_val:
                b=b.next
                a=a.next
            else:
                while b.val>pivo_val:
                    b=b.next
                temp=b.val
                b.val=a.val
                a.val=temp
                a=a.next
                if not b.next:
                    break
            print(self)
            print(a)
            print(b)
            print('--------')
        
        
a = linked_list(5)
a.add_val(1)
a.add_val(8)
a.add_val(0)
a.add_val(3)

