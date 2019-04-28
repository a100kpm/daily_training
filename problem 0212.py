'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Dropbox.

Spreadsheets often use this alphabetical encoding for its columns: "A", "B", "C", ..., "AA", "AB", ..., "ZZ", "AAA", "AAB", ....

Given a column number, return its alphabetical column id. For example, given 1, return "A". Given 27, return "AA".
'''


import math

    
def test(num):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    num_cop=num
    start=26
    compteur=1
    while start<num_cop:
        num_cop=num_cop-start
        start=start*26
        compteur+=1
        
    result=[0]*compteur

    start=start/26
    
    for i in range(compteur):
        if start>=num and start!=1:
            result[i-1]-=1
            num+=start*26
        rez=math.floor(num/start)
        if num%start==0 and start!=1:
            rez=rez-1
        result[i]=rez
        num=num-rez*start
        start=start/26
    alpha_column_id=""
    for i in range(compteur):
        alpha_column_id+=alphabet[result[i]-1]
        
    return alpha_column_id


    