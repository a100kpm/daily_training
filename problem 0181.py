'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given a string, split it into as few strings as possible such that each string is a palindrome.

For example, given the input string racecarannakayak, return ["racecar", "anna", "kayak"].

Given the input string abc, return ["a", "b", "c"].
'''

word ='racecarannakayak'
word2='abc'
word3='racecaraannakayak'
# should return ["racecar","a","anna","kayak"]

def is_palindrom(word):
    lenn=len(word)
    for i in range(lenn):
        if word[i]==word[lenn-i-1]:
            pass
        else:
            return False
    return True

def giff_palindrom(word):
    List=[]
    compteur=[]
    lenn=len(word)
    for i in range(1,lenn+1):
        if is_palindrom(word[:i]):
            List.append([ word[:i] ])
#            compteur.append(i)
            if len(word[i:])>=1:

                List[-1].extend(giff_palindrom(word[i:]))
            

    for i in range(len(List)):
        size.append(len(List[i]))
    min_=min(size)
    index_min=size.index(min_)
    
    return List[index_min]