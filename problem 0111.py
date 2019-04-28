'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given a word W and a string S, find all starting indices in S which are anagrams of W.

For example, given that W is "ab", and S is "abxaba", return 0, 3, and 4
'''


W = "ab"
S = "abxaba"

def first_letter_anagram(W,S):
    lenn=len(S)
    lenn2=len(W)
    pos=[]
    max_loop=lenn-lenn2+1
    
    for i in range(max_loop):
        current_letter=S[i:i+lenn2]
        if anagram(current_letter,W)==True:
            pos.append(i)
            
    return pos

def anagram(current_letter,W):
    lenn=len(current_letter)
    for i in range(lenn):
        if current_letter[i] in W:
            a=W.index(current_letter[i])
            W=W[:a]+W[a+1:]
            
        else:
            return False
    return True