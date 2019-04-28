'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Dropbox.

Given a string s and a list of words words, where each word is the same length, 
find all starting indices of substrings in s that is a concatenation of every word in words exactly once.

For example, given s = "dogcatcatcodecatdog" and words = ["cat", "dog"], 
return [0, 13], since "dogcat" starts at index 0 and "catdog" starts at index 13.

Given s = "barfoobazbitbyte" and words = ["dog", "cat"], return [] 
since there are no substrings composed of "dog" and "cat" in s.

The order of the indices does not matter.
'''


s1 = "dogcatcatcodecatdog"
s2 = "barfoobazbitbyte"
words1 = ["cat", "dog"]
words2 = ["dog", "cat"]


def find_start_concatene(s,word):
    if word==[]:
        return None
    set_=set()
    for i in word:
        set_.add(i)
        
    set_temp=set_.copy()
    i=0
    lenn=len(s)
    size=len(word[0])
    compteur=[]
    start_val=-1
    while i<=lenn-size:
        if s[i:i+size] in set_temp:
            set_temp.remove(s[i:i+size])
            if start_val==-1:
                start_val=i
            i+=size
        else:
            i+=1
            set_temp=set_.copy()
            start_val=-1
        if len(set_temp)==0:
            compteur.append(start_val)
            start_val=-1
            set_temp=set_.copy()
    return compteur