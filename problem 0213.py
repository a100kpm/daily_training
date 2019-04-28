'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Snapchat.

Given a string of digits, generate all possible valid IP address combinations.

IP addresses must follow the format A.B.C.D, where A, B, C, and D are numbers between 0 and 255. 
Zero-prefixed numbers, such as 01 and 065, are not allowed, except for 0 itself.

For example, given "2542540123", you should return ['254.25.40.123', '254.254.0.123'].
'''

number = "2542540123"

def giff_ip(number,stage=0,ip=""):
    if len(number)==0:
        return
    stoppper=False
    if number[0]=='0':
        stoppper=True
        
    lenn=len(number)
    if stage==0:
        i=0
        listing=[]
        while i<lenn and i<3:
            if int(number[:i+1])<=255:
                a=giff_ip(number[i+1:],stage+1,ip+number[:i+1])
                if a!=None and a!=[]:
                    listing.extend(a)
            if stoppper==True:
                i=4
            i+=1
        
    elif stage<3:
        i=0
        listing=[]
        while i<lenn and i<3:
            if int(number[:i+1])<=255:
                a=giff_ip(number[i+1:],stage+1,ip+'.'+number[:i+1])
                if a!=None and a!=[]:
                    listing.extend(a)
            if stoppper==True:
                i=4
            i+=1
    
    
    if stage==3:
        if lenn>=4:
            return
        
        if int(number)<=255:
            return [ip+'.'+number]
        return
    
    return listing

