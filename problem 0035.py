'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given an array of strictly the characters 'R', 'G', and 'B', 
segregate the values of the array so that all the Rs come first, 
the Gs come second, and the Bs come last. You can only swap elements of the array.

Do this in linear time and in-place.

For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], 
it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
'''

hurray = ['G', 'B', 'R', 'R', 'B', 'R', 'G']

def order_RGB(hurray):
    lenn=len(hurray)
    Find_R=True
    Find_G=True
    i=0
    while i<lenn:
        if Find_R==True:
        
            for j in range(i+1,lenn):
                print(j)
                if hurray[j]=='R':
                    hurray[j]=hurray[i]
                    hurray[i]='R'
                    break
                if j==(lenn-1):
                    Find_R=False
                    i=i-1
                    
                
        elif Find_G==True: 
            
            for j in range(i+1,lenn):
                if hurray[j]=='G':
                    hurray[j]=hurray[i]
                    hurray[i]='G'
                    break
                    
                if j==lenn-1:
                    Find_G=False
                
        i+=1
    return hurray
                    
                    