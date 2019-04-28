'''
Good morning! Here's your coding interview problem for today.

This problem was asked by IBM.

Given a string with repeated characters, rearrange the string so that no two adjacent 
characters are the same. If this is not possible, return None.

For example, given "aaabbc", you could return "ababac". Given "aaab", return None.
'''

string1="aaabbc"
string2="aaab"
string3="abcabcabcabcabcdd"
string4="abcabcabcabcabcdda"

def rearrenge_letter(string):
    a=dict()
    for i in string:
        if i not in a:
            a[i]=1
        else:
            a[i]+=1
            
    

    word=''
    last_use=''
    
    while len(a)>0:
        letter=sorted(a,key=a.get,reverse=True)[0]
        
        
        if last_use==letter:
            if len(a)==1:
                return None
            letter=sorted(a,key=a.get,reverse=True)[1]
            

        word+=letter
        a[letter]-=1
        if a[letter]==0:
            a.pop(letter)
        last_use=letter
            
    return word
            
            
            