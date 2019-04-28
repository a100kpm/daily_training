'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Dropbox.

Given a list of words, determine whether the words can be chained to form a circle.
A word X can be placed in front of another word Y in a circle if the last character of X is same as the first character of Y.

For example, the words ['chair', 'height', 'racket', touch', 'tunic'] 
can form the following circle: chair --> racket --> touch --> height --> tunic --> chair.
'''

List = ['chair', 'height', 'racket', 'touch', 'tunic','c']

def can_cycle(List):
    dico1=dict()
    dico2=dict()
    dico3=dict()
    for i in List:
        if i[0]==i[-1]:
            if i[0] not in dico3:
                dico3[i[0]]=1
        else:
            if i[0] not in dico1:
                dico1[i[0]]=1
                dico2[i[0]]=0
                
            else:
                dico1[i[0]]+=1
                
            if i[-1] not in dico2:
                dico1[i[-1]]=0
                dico2[i[-1]]=1
            
            else:
                dico2[i[-1]]+=1
            
    for i in dico1:
        if dico1[i]!=dico2[i]:
            return False
        
    for i in dico3:
        if i not in dico1:
            return False
        
    return True