'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given a string of parentheses, find the balanced string that can be produced 
from it using the minimum number of insertions and deletions.
If there are multiple solutions, return any of them.

For example, given "(()", you could return "(())". Given "))()(", you could return "()()()()"
'''

test1="(()"
test2="))()("

def balanced_brackets(bracket_list):
    List=[]
    compteur=[]
    lenn=len(bracket_list)
    prev=None
    for i in range(lenn):
        List.append(bracket_list[i])
        compteur.append(i)
        if bracket_list[i]==")" and prev=="(":
            List=List[:-2]
            compteur=compteur[:-2]
            
        prev=List[-1]
        
        
    new_bracket=''
    for i in range(lenn):
        if i in compteur:
            pass
        else:
            new_bracket+=bracket_list[i]
            
    return new_bracket

            
    
    
    
    
    
    
