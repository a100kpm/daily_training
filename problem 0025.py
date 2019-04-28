'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Implement regular expression matching with the following special characters:

    . (period) which matches any single character
    * (asterisk) which matches zero or more of the preceding element

That is, implement a function that takes in a string and a valid regular expression 
and returns whether or not the string matches the regular expression.

For example, given the regular expression "ra." and the string "ray",
 your function should return true. The same regular expression on the string "raymond" should return false.

Given the regular expression ".*at" and the string "chat", 
your function should return true. The same regular expression on the string "chats" should return false.
'''

regular = "ra."
string = "ray"

regular2 = ".*at"
string2 = "chat"
strings2 = "chats"

def express_matcher(regular,string):
    if '*' in regular:
        is_etoile=True
    else:
        is_etoile=False
    lenn=len(string)  
    lenn2=len(regular)
    if is_etoile==False:
        
        if lenn==lenn2:
            for i in range(lenn):
                if regular[i]!= ".":
                    if regular[i]!=string[i]:
                        return False
            return True
        else:
            return False
    
        
    i=0
    j=0
    while j<lenn and i<lenn2:
        if regular[i]==".":
            i+=1
            j+=1
        elif regular[i]!="*":
            if regular[i]==string[j]:
                i+=1
                j+=1
            else:
                return False
        else:
            if i+1==lenn2:
                return True
            new_string=string[j:]
            new_regular=regular[i+1:]
            List=[]
            for k in range(j,lenn):
                List.append(express_matcher(new_regular,new_string))
                new_string=new_string[1:]
            if True in List:
                return True
            return False
                
            
            
            
            
            
    