'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given a string of round, curly, and square open and closing brackets, 
return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
'''

string1="([])[]({})"
string2="([)]"
string3="((()"

def well_rounded(string):
    lenn=len(string)
    List=[]
    for i in range(lenn):
        if string[i]=='(' or string[i] == '[' or string[i] == '{':
            List.append(string[i])
        elif len(List)==0:
            return False
        elif string[i]==']' and List[len(List)-1]=='[' or string[i]==')' and List[len(List)-1]=='(' or string[i]=='}' and List[len(List)-1]=='{':

            List=List[:len(List)-1]
        else:
            return False
    if len(List)==0:
        return True
    return False

