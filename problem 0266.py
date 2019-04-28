'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Pivotal.

A step word is formed by taking a given word, adding a letter, and anagramming the result. 
For example, starting with the word "APPLE", you can add an "A" and anagram to get "APPEAL".

Given a dictionary of words and an input word, create a function that returns all valid step words.
'''
word='apple'
dictionnary=set()
dictionnary.add('appeal')
dictionnary.add('lapple')
dictionnary.add('rofllol')

def all_anagram(letter,word=""):
    lenn=len(letter)
    
    if lenn==0:
        return word
    
    result=[]
    
    for i in range(lenn):
        val=all_anagram(letter[:i]+letter[i+1:],word+letter[i])
        if type(val)==list:
            result.extend(val)
        else:
            result.append(val)
        
    return result


def step_word(word,dictionnary):
    List_word=[]
    lettre='abcdefghijklmnopqrstuvwxyz'
    for i in lettre:
        List_word.extend(all_anagram(word+i))
        
    result=set()
    
    for i in List_word:
        if i not in result and i in dictionnary:
                result.add(i)
                
    return result