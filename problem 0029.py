'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Run-length encoding is a fast and simple method of encoding strings. 
The basic idea is to represent repeated successive characters as a single count and character.
For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. 
You can assume the string to be encoded have no digits and consists solely of
 alphabetic characters. You can assume the string to be decoded is valid.
'''


string = "AAAABBBCCDAA"

def encodeur(string):
    retour = []
    lenn=len(string)
    retour.append([string[0],1])
    j=0
    for i in range(1,lenn):
        if string[i]==retour[j][0]:
            retour[j][1]+=1
        else:
            j+=1
            retour.append([string[i],1])
    lenn2=len(retour)
    encodage=''
    for i in range(lenn2):
        encodage=encodage+str(retour[i][1])+retour[i][0]
        
    return encodage