'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Epic.

The "look and say" sequence is defined as follows: beginning with the term 1, 
each subsequent term visually describes the digits appearing in the previous term. 
The first few terms are as follows:

1
11
21
1211
111221

As an example, the fourth term is 1211, since the third term consists of one 2 and one 1.

Given an integer N, print the Nth term of this sequence.
'''


def look_and_say(n,seq='1'):
    if n==1:
        return seq
    new_seq=''
    last_num=seq[0]
    nbr_last_num=1
    
    for i in seq[1:]:
        if i==last_num:
            nbr_last_num+=1
        else:
            new_seq=new_seq+str(nbr_last_num)+last_num
            last_num=i
            nbr_last_num=1
            
    new_seq=new_seq+str(nbr_last_num)+last_num
    
    return look_and_say(n-1,new_seq)
