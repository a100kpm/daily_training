'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given a string of parentheses, write a function to compute the minimum number of 
parentheses to be removed to make the string valid (i.e. each open parenthesis is eventually closed).

For example, given the string "()())()", you should return 1. Given the string ")(", 
you should return 2, since we must remove all of them.
'''


string1='()())()'
string2=')('

def nbr_delete_paran(string):
    total_remove=0
    stop=False
    while stop==False:
        stop=True
        lenn = len(string)
        count1=0
        count2=0
        
        for i in range(lenn):
            if string[i]=='(':
                count1+=1
            else:
                count2+=1
            
            if count2==count1 and count2!=0:
                string=string[i+1:]
                stop=False
                break
            elif count2>count1:
                string=string[1:]
                total_remove+=1
                stop=False
                break
            

    if len(string)==1:
        total_remove+=1
        
    return total_remove
            
            