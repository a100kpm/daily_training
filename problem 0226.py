'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Airbnb.

You come across a dictionary of sorted words in a language you've never seen 
before. Write a program that returns the correct order of letters in this language.

For example, given ['xww', 'wxyz', 'wxyw', 'ywx', 'ywz'], you should return ['x', 'z', 'w', 'y'].
'''


List= ['xww', 'wxyz', 'wxyw', 'ywx', 'ywz']


def order_letter(List):
    lenn=len(List)
    letter=set()
    order=[]
    for i in List:
        for j in i:
            if j in letter:
                pass
            else:
                letter.add(j)
                
    compteur=len(letter)
    number_letter=-1
    while compteur>0:
        
        number_letter+=1
        List_word=create_set_word(List,number_letter)
#        ignore set vide ou d'un seul elem
        List_word=Treat_list_word(List_word)
        
        
def create_set_word(List,number_letter):
    result=[]
    current_result=[]
    
    lenn=len(List)
    prev_base_word=List[0][:number_letter]
    if len(List[0])>=number_letter+1:
        current_result.append(List[0][:number_letter+1])
    for i in range(1,lenn):
        if List[i][:number_letter]==prev_base_word:
            if len(List[i])>=number_letter+1:
                current_result.append(List[i][:number_letter+1])
        else:
            result.append(current_result)
            current_result=[]
            if len(List[i])>=number_letter:
                prev_base_word=List[i][:number_letter]
                if len(List[i])>=number_letter+1:
                    current_result.append(List[i][:number_letter+1])
    if current_result!=[]:
        result.append(current_result)
        
    return [[]]+result
# =============================================================================
# wrong wrong wrong wrong wrong
# def Treat_list_word(List_word):
#     for i in List_word:
#         print(i)
#         if len(i)<=1:
#             del(List_word[List_word==i])
#         else:
#             for j in i:
#                 j=j[-1]
#                 
#     return List_word
# =============================================================================
        

# to finish
    
    
    
    
    
    
    
    
    
    
    
    
    