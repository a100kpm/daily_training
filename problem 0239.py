'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Uber.

One way to unlock an Android phone is through a pattern of swipes across a 1-9 keypad.

For a pattern to be valid, it must satisfy the following:

    All of its keys must be distinct.
    It must not connect two keys by jumping over a third key, unless that key has already been used.

For example, 4 - 2 - 1 - 7 is a valid pattern, whereas 2 - 1 - 7 is not.

Find the total number of valid unlock patterns of length N, where 1 <= N <= 9.
'''



def is_valid(word,number):
    if len(word)==0:
        return True
    if number in word:
        return False
    allow=[(2,4,5),(1,3,4,5,6),(2,5,6),(1,2,5,8,7),(1,2,3,4,6,7,8,9),(3,2,5,8,9),(4,5,8),(7,4,5,6,9),(8,5,6)]
        
    for i in word:
        if number in allow[i-1]:
            return True
    
    return False

def number_valid(word=[],size=9):
    if size==0:
        return 1
    
    List_word=[]
    for i in range(1,10):
        if is_valid(word,i)==True:
            word_temp=word.copy()
            word_temp.append(i)
            List_word.append(word_temp)
                    
    score =0
    for i in range(len(List_word)):
        score+=number_valid(List_word[i],size-1)
        
    return score

result=0
for i in range(1,10):
    a=number_valid(size=i)
    print(a)
    result+=a
    
print('result=',result)
