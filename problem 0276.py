'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Dropbox.

Implement an efficient string matching algorithm.

That is, given a string of length N and a pattern of length k, 
write a program that searches for the pattern in the string 
with less than O(N * k) worst-case time complexity.

If the pattern is found, return the start index of its location. If not, return False.
'''

#boyer moore algorithm
#still (O(N*k)) is case like pattern= 'aaa' string = 'aaaaaaaa'


pattern='abac'
string='abacbaaccabaccaab'

def find_pattern_index(pattern,string):
    lenn=len(string)
    lenn2=len(pattern)
    result=[]
    curseur=lenn2-1
    
    while curseur<lenn:
        find=True
        for checker in range(lenn2-1):
            if pattern[lenn2-1-checker]!=string[curseur-checker]:

                caracter=pattern[lenn2-1-checker]
                find=False
                break
            
        if find==True:
            result.append(curseur-lenn2+1)
            curseur+=1
        else:
            while curseur<lenn and string[curseur]!=caracter:
                curseur+=1
            curseur=curseur+checker

            

    return result
            
            