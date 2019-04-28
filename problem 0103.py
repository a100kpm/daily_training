'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Square.

Given a string and a set of characters, return the shortest substring containing all the characters in the set.

For example, given the string "figehaeci" and the set of characters {a, e, i}, you should return "aeci".

If there is no substring containing all the characters in the set, return null.
'''

string="figehaecifff"
characters = {'a', 'e', 'i'}


def min_substring_contain(string,characters):
    List=[]
    for i in characters:
        List.append(i)
    lenn=len(List)
    lenn2=len(string)          
    
    min_val=0
    min_chara=[]
    for i in range(lenn2):
        current_List=string[i:]
        if len(current_List)<lenn:
            break
        position_first=[]
        for j in range(lenn):
            if List[j] in current_List:
                position_first.append(current_List.index(List[j]))
            else:
                break
        if len(position_first)<len(List):
            break
        else:
            val=max(position_first)+1
            if min_val==0:
                min_val=val
                min_chara=current_List[:min_val]
            else:
                if min_val>val:
                    min_val=val
                    min_chara=current_List[:min_val]
    
        
    
    
    
    if min_val==0:
        return None
    return min_chara
    
    