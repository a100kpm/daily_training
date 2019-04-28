'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given a string which we can delete at most k, return whether you can make a palindrome.

For example, given 'waterrfetawx' and a k of 2, you could delete f and x to get 'waterretaw'.
'''

string = 'waterrfetawx'
k = 2

def can_palindrome_with_delete(string,k):
    if len(string)<=1:
        return True
    if string[0]==string[-1]:
        return can_palindrome_with_delete(string[1:-1],k)
    else:
        if k>0:
            return can_palindrome_with_delete(string[1:],k-1) or can_palindrome_with_delete(string[:-1],k-1)
    return False