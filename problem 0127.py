'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

Let's represent an integer in a linked list format by having each node represent a digit in the number.
 The nodes make up the number in reversed order.

For example, the following linked list:

1 -> 2 -> 3 -> 4 -> 5

is the number 54321.

Given two linked lists in this format, return their sum in the same linked list format.

For example, given

9 -> 9

5 -> 2

return 124 (99 + 25) as:

4 -> 2 -> 1
'''
import math

class linked_list:
    def __init__(self,val):
        if abs(val)<10:
            self.val = val
            self.suivant = None
        else:             
            a=val%10
            val_temp=math.floor(val/10)
            self.val=a
            self.suivant = linked_list(val_temp)
            
    def val_printer(self):
        print(self.val)
        if self.suivant:
            self.suivant.val_printer()
            
def linked_list_sommeur(val1,val2):
    result = val1.val+val2.val
    retenu=0
    if result>=10:
        result-=10
        retenu=1
    link=linked_list(result)
        
    suiv=link
    while val1.suivant or val2.suivant:
        if val1.suivant:
            val1=val1.suivant
            val1_val=val1.val
        else:
            val1_val=0
        if val2.suivant:
            val2=val2.suivant
            val2_val=val2.val
        else:
            val2_val=0
            
        result = val1_val+val2_val+retenu
        retenu=0
        if result>=10:
            result-=10
            retenu=1
        
        suiv.suivant=linked_list(result)
        suiv=suiv.suivant
    if retenu==1:
        suiv.suivant=linked_list(1)
    
    return link
            
            
#val1 = linked_list(54321)
val2= linked_list(99)
val1= linked_list(25)
print('val2')
val2.val_printer()
print('val1')
val1.val_printer()

