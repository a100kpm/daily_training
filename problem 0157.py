'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Given a string, determine whether any permutation of it is a palindrome.

For example, carrace should return true, since it can be rearranged to form racecar,
 which is a palindrome. daily should return false, since there's no rearrangement that can form a palindrome.
'''
 

word ='carrace'

def can_palindrom(word):
    dictio=dict()
    lenn=len(word)
    for i in range(lenn):
        if word[i] not in dictio:
            dictio[word[i]]=0
        dictio[word[i]]+=1
        

    compteur=0
    for i in dictio:
        compteur+=dictio[i]%2
    if compteur>1:
        return False
    return True
        