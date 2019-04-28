'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

You're given a string consisting solely of (, ), and *. * can represent 
either a (, ), or an empty string. Determine whether the parentheses are balanced.

For example, (()* and (*) are balanced. )*( is not balanced.
'''

string1 = '(()*'
string2 =  '(*)'
string3 = ')*('

def balanced(string,listing=''):
    if len(string)==0:
        result = reductor(listing)
        if len(result)==0:
            print('balanced')
            return True
        else:
            return False
    else:
        if string[0]!='*':
            return balanced(string[1:],listing+string[0])
        else:
            return balanced(string[1:],listing+')') or balanced( string[1:],listing+'(' ) or balanced(string[1:],listing)
        
        
def reductor(listing):
    lenn=len(listing)
    
    string_temp=''
    last_elem=''
    for i in range(lenn):
        if last_elem=='(' and listing[i]==')':
            string_temp=string_temp[:-1]
            if len(string_temp)==0:
                last_elem=''
            else:
                last_elem=string_temp[-1]
        else:
            string_temp+=listing[i]
            last_elem=listing[i]
            
    return string_temp
