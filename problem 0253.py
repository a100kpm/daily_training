'''
Good morning! Here's your coding interview problem for today.

This problem was asked by PayPal.

Given a string and a number of lines k, print the string in zigzag form. In zigzag, 
characters are printed out diagonally from top left to bottom right until reaching the kth line, 
then back up to top right, and so on.

For example, given the sentence "thisisazigzag" and k = 4, you should print:

t     a     g
 h   s z   a
  i i   i z
   s     g

'''

word = "thisisazigzag"
k = 4


def print_zigzag(word,k):
    if k==1:
        print(word)
        return
    lenn=len(word)
    pos=0
    List=[]
    for i in range(lenn):
        List.append(pos)
        if pos==k-1:
            sens=False
        elif pos==0:
            sens=True
            
        if sens==True:
            pos+=1
        else:
            pos-=1
            
    for i in range(k):
        new_word=""
        for j in range(lenn):
            if List[j]==i:
                new_word+=word[j]
            else:
                new_word+=" "
                
        print(new_word)
        
