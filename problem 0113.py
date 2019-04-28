'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given a string of words delimited by spaces, reverse the words in string. 
For example, given "hello world here", return "here world hello"

Follow-up: given a mutable string representation, can you perform this operation in-place?
'''

string = "here world hello"

def reverse_word_order(string):
    a=string.split(' ')
    b=""
    lenn=len(a)
    for i in range(lenn-1,-1,-1):
        b+=a[i]
        b+=" "
    return b[:-1]


def reverse_word_order_mutable(string):
    pass


        