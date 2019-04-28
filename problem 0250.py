'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

A cryptarithmetic puzzle is a mathematical game where the digits of some numbers 
are represented by letters. Each letter represents a unique digit.

For example, a puzzle of the form:

  SEND
+ MORE
--------
 MONEY

may have the solution:

{'S': 9, 'E': 5, 'N': 6, 'D': 7, 'M': 1, 'O', 0, 'R': 8, 'Y': 2}

Given a three-word puzzle like the one above, create an algorithm that finds a solution.
'''

import random


List='abcdefghijklmnopqrstuvwxyz'

word1=''
word2=''
word3=''

for i in range(3):
    word1+=List[random.randrange(0,26)]
    word2+=List[random.randrange(0,26)]
    word3+=List[random.randrange(0,26)]

word3+=List[random.randrange(0,26)]

print(word1)
print(word2)
print(word3)

def solveur(word1,word2,word3):    
    for i in range(1000):
        for j in range(1000):
            valid,dict_1=valid1(i,word1)
            if valid==True:
                valid,dict_tot=valid2(dict_1,j,word2)
                if valid==True:
                    valid,dict_=valid3(dict_tot,i+j,word3)
                    if valid==True:
                        dict_.pop('un_elem')
                        return dict_
                    
    print('no sol')
    return None

def valid1(i,word1):
    dict_=dict()
    i=str(i)
    dict_['un_elem']='trotinette'
    if len(i)<3:
        return False,dict_
    compteur=[]
    
    for aa in range(3):
        if word1[aa] not in dict_:
            for name,val in dict_.items():
                compteur.append(val)
            if i[aa] not in compteur:
                dict_[word1[aa]]=i[aa]
            else:
                return False,dict_
        else:
            if i[aa]!=dict_[word1[aa]]:
                return False,dict_
    return True,dict_
                

def valid2(dict_,j,word2):
    j=str(j)
    dict_['un_elem']='trotinette'
    if len(j)<3:
        return False,dict_

    compteur=[]
    for aa in range(3):
        if word2[aa] not in dict_:
            for name,val in dict_.items():
                compteur.append(val)
            if j[aa] not in compteur:
                dict_[word2[aa]]=j[aa]

            else:
                return False,dict_
        else:
            if j[aa]!=dict_[word2[aa]]:
                return False,dict_
    return True,dict_

def valid3(dict_,nbr,word3):
    nbr='0'+str(nbr)
    nbr=nbr[-4:]
    compteur=[]
    if len(nbr)<4:
        return False,dict_
    dict_['un_elem']='trotinette'
    for aa in range(3):
        if word3[aa] not in dict_:
            for name,val in dict_.items():
                compteur.append(val)
            if nbr[aa] not in compteur:
                dict_[word3[aa]]=nbr[aa]

            else:
                return False,dict_
        else:
            if nbr[aa]!=dict_[word3[aa]]:
                return False,dict_
    return True,dict_
        
word1='aaa'
word2='bbb'
word3='dccc'
        
        
        
        
                
                
                
            