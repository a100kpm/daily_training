'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Palantir.

Write an algorithm to justify text. Given a sequence of words and an integer line length k, 
return a list of strings which represents each line, fully justified.

More specifically, you should have as many words as possible in each line. 
There should be at least one space between each word.
 Pad extra spaces when necessary so that each line has exactly length k. 
 Spaces should be distributed as equally as possible, with the extra spaces, 
 if any, distributed starting from the left.

If you can only fit one word on a line, then you should pad the right-hand side with spaces.

Each word is guaranteed not to be longer than k.

For example, given the list of words 
["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] 
and k = 16, you should return the following:

["the  quick brown", # 1 extra space on the left
"fox  jumps  over", # 2 extra spaces distributed evenly
"the   lazy   dog"] # 4 extra spaces distributed evenly
'''



List=["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] 
k=16

def justifier(List,k):
    lenn=len(List)
    long_word=[]
    for i in range(lenn):
        long_word.append(len(List[i]))
    words=[]
    compteur=0
    for i in range(lenn):
        if compteur+long_word[i]+1<=k:
            compteur+=long_word[i]+1
        else:
            words.append([i-1,compteur])
            compteur=long_word[i]+1
    words.append([lenn-1,compteur])
    
    lenn2= len(words)
    for i in range(lenn2):
        words[i][1]=17-words[i][1]
    lim_word=0
    justified=[]
    k=0
    for i in range(lenn):
        if i!=words[k][0]:
            List[i]+=' '
        else:
            k+=1
    for i in range(lenn2):
        k=lim_word
        while words[i][1]>0:
            words[i][1]-=1
            List[k]+=' '
            k+=1
            if k==words[i][0]:
                k=lim_word
        justified.append(List[lim_word:words[i][0]+1])
        lim_word=words[i][0]+1
    lenn3=len(justified)
    return_justified=[]
    for i in range(lenn3):
        a=''
        for g in justified[i]:
            a+=g
        return_justified.append(a)
    return return_justified
            
            
            
            

        
        
        