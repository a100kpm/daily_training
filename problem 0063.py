'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

Given a 2D matrix of characters and a target word, write a function that returns
 whether the word can be found in the matrix by going left-to-right, or up-to-down.

For example, given the following matrix:

[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]

and the target word 'FOAM', you should return true, since it's the leftmost column.
 Similarly, given the target word 'MASS', you should return true, since it's the last row.
'''

import numpy as np

word= 'FOAM'
word2= 'MASS'
word3 = 'AAAAA'
word4= 'MASSS'

matrix = np.array([['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']])

def word_finder(matrix,word):
    first_letter = word[0]
    size=len(word)
    lenn=np.shape(matrix)[0]
    lenn2=np.shape(matrix)[1]
    
    for i in range(lenn):
        for j in range(lenn2):
            if matrix[j][i]==first_letter:
#                print('i={} and j={}'.format(i,j))
                horizontal=i
                vertical=j
                ok=True
                n=1
                while horizontal < lenn2-1 and ok ==True:
                    horizontal+=1
                    n+=1
                    if word[n-1]!=matrix[j][horizontal]:
                        ok=False
                    if n==size and ok==True:
                        return True
                ok=True
                n=1
                while vertical < lenn-1 and ok ==True:
                    vertical+=1
                    n+=1
                    if word[n-1]!=matrix[vertical][i]:
                        ok=False
                    if n==size and ok==True:
                        return True
    return False
                    
    