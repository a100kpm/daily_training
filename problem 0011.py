'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string s and a set of all possible query strings,
return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
'''

dictio = ['dog', 'deer', 'deal', 'alert']

def preprocess_strings(strings):
    import numpy as np
    return np.sort(strings)


def query(string,dictio,preprocess=False):
    lenn = len(dictio)
    search=len(string)
    List=[]
    if preprocess==True:
        dictio = preprocess_strings(dictio)
        stop=True
        n=0
        while stop:
            if dictio[n][:search]==string:
                List+=[dictio[n]]
            elif len(List)!=0:
                stop=False
            n+=1
            
    else: 
        for n in range(lenn):
            if dictio[n][:search]==string:
                List+=[dictio[n]]
    return List

print(query('de',dictio,preprocess=True))