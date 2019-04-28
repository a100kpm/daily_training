'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Given an integer k and a string s, find the length of the longest substring 
that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring 
with k distinct characters is "bcb".
'''

string = "abcba"
k = 2

def search_substring(string,diff):
    saved_string=''
    saved_leng=0
    lenn=len(string)
    i=0
    
    while i+saved_leng<=lenn:
        j=i
        current_list=''
        current_letter=[]
        current_leng=0
        while j<lenn and current_leng<=diff:
            if string[j] not in current_letter:
                if current_leng<diff:
                    current_letter+=string[j]
                    current_list+=string[j]
                    current_leng+=1
                else:
                    j=lenn
            else:
                current_list+=string[j]
                current_leng+=1
            j+=1
            
            
        if current_leng>saved_leng:
            saved_string=current_list
            saved_leng=len(saved_string)
        i+=1
    return saved_string
                
                
        