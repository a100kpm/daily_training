'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

UTF-8 is a character encoding that maps each symbol to one, two, three, or four bytes.

For example, the Euro sign, €, corresponds to the three bytes 11100010 10000010 10101100. The rules for mapping characters are as follows:

    For a single-byte character, the first bit must be zero.
    For an n-byte character, the first byte starts with n ones and a zero. The other n - 1 bytes all start with 10.

Visually, this can be represented as follows.

 Bytes   |           Byte format
-----------------------------------------------
   1     | 0xxxxxxx
   2     | 110xxxxx 10xxxxxx
   3     | 1110xxxx 10xxxxxx 10xxxxxx
   4     | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx

Write a program that takes in an array of integers representing byte values, and returns whether it is a valid UTF-8 encoding.
'''
array1=[0,0,0,0,0,0,0,0]
array2=[0,0,0,0,0,0,0,0,0]
array3=[1,1,0,1,1,1,1,1,1,0,0,0,0,0,0,0]
array4=[1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1]

def valid_byte(array):

    
    lenn=len(array)
    
    compteur=0
    
    while compteur<lenn:
        compteur,validation=check_valid(array,compteur)
        if validation==False or compteur>lenn:
            return False
        
    return True

def check_valid(array,compteur):
    valid=[0,1]
    
    if array[compteur]==0:
        for i in array[compteur:compteur+8]:
            if i not in valid:
                return compteur,False
        return compteur+8,True
    elif array[compteur:compteur+3]==[1,1,0]:
        if array[compteur+8:compteur+8+2]==[1,0]:
            for i in array[compteur:compteur+16]:
                if i not in valid:
                    return compteur,False
        else:
            return compteur,False
        return compteur+16,True
        
    elif array[compteur:compteur+4]==[1,1,1,0]:
        if array[compteur+8:compteur+8+2]==[1,0] and array[compteur+16:compteur+16+2]==[1,0]:
            for i in array[compteur:compteur+24]:
                if i not in valid:
                    return compteur,False
        else:
            return compteur,False
        return compteur+24,True
        
    elif array[compteur:compteur+5]==[1,1,1,1,0]:
        if array[compteur+8:compteur+8+2]==[1,0] and array[compteur+16:compteur+16+2]==[1,0] and array[compteur+24,compteur+26]==[1,0]:
            for i in array[compteur:compteur+32]:
                if i not in valid:
                    return compteur,False
        else:
            return compteur,False
        return compteur+30,True
        
    else:
        return compteur,False
