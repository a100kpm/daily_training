'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given a string, return the first recurring character in it, or null if there is no recurring character.

For example, given the string "acbbac", return "b". Given the string "abcdef", return null.
'''

string="acbbac"
string1="abcdef"

def find_dual(string):
    lenn=len(string)
    set_=set()
    for i in range(lenn):
        if string[i] not in set_:
            set_.add(string[i])
        else:
            return string[i]
    return None