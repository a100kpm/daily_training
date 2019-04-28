'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

Given a dictionary of words and a string made up of those words (no spaces),
 return the original sentence in a list. If there is more than one possible reconstruction,
 return any of them. If there is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string 
"thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string
 "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].
'''

List1=['bed','bath','bedbath','and','beyond']
List2=['quick','brown','the','fox']

string1='bedbathandbeyond'
string2='thequickbrownfoxy'

def sentence_in_list(List_,String_):

    lenn=len(List_)
    lenn2=len(String_)
    Stock=[]

    ok=True
    while ok==True:    
        Nfound=False
        i=1
        while Nfound==False:
            
            if i>len(String_):
                return None
            courant=String_[0:i]
            
            
            for j in range(lenn):
                if List_[j]==courant:
                    Nfound=True
                    Stock.append(courant)
                    String_=String_[i:]
                    
                    break
            i+=1     
        if len(String_)==0:
            ok=False

    return Stock
        
            
        