'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given a string consisting of parentheses, single digits, and positive and negative signs, 
convert the string into a mathematical expression to obtain the answer.

Don't use eval or a similar built-in parser.

For example, given '-1 + (2 + 3)', you should return 4.
'''

string = '-1 + (2 + 3)'


def evalution(string):
    i=0
    while i<len(string):
        if string[i]==' ':
            string=string[:i]+string[i+1:]
        else:
            i+=1
          

     
    i=0
    while i<len(string):
        if string[i]=='(':
            string=calc(string,i+1)
        else:
            i+=1
            
    return int(calcul_str_expr(string))
    
    

def calc(string,start):

    
    i=start
    while i<len(string):
        if string[i]=='(':
            string=calc(string,i+1)
            
        elif string[i]==')':
            rez=calcul_str_expr(string[start:i])
            string=string[:start-1]+rez+string[i+1:]
            return string
        i+=1
        
    print('parenthesis error')
    
def calcul_str_expr(string):
    operateur='+-'
    nbr='1234567890'
    num_cache=''
    last_sign='+'
    rez=0
    i=0
    if string[0]=='-':
        i=1
        last_sign='-'
        
    lenn=len(string)
    while i<lenn:
        if string[i]=='-' and num_cache=='':
            if string[i-1]=='-':
                last_sign='+'
            else:
                last_sign='-'
                
        elif string[i]=='+' and num_cache=='':
            last_sign='+'
            
        elif string[i] in nbr:
            num_cache+=string[i]
            
        elif string[i] in operateur:
            if last_sign=='+':
                rez+=int(num_cache)
            else:
                rez-=int(num_cache)
                
            num_cache=''
            last_sign=string[i]
            
        i+=1
        
    if last_sign=='+':
        rez+=int(num_cache)
    else:
        rez-=int(num_cache)
        
    return str(rez)
        
        
        
        
        
        
        
        
            
        
    
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            