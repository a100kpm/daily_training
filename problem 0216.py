'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given a number in Roman numeral format, convert it to decimal.

The values of Roman numerals are as follows:

{
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}
'''

dictio={
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}


#sort the dictionnary by value (under list format):
#dictio = sorted(dictio,key=dictio.get,reverse=True)
import numpy as np

def roman_value(number,dictio):
    if len(number)==1:
        return dictio[number]
    
    result=0
    
    if dictio[number[0]]<dictio[number[1]]:
        result-=dictio[number[0]]
        number=number[1:]
        
    lenn=len(number)-1
    
    for i in range(lenn):
        if dictio[number[i]]<dictio[number[i+1]]:
            result-=dictio[number[i]]
        else:
            result+=dictio[number[i]]
            
    result+=dictio[number[-1]]
    
    
    return result
    
    
    

            
    
    