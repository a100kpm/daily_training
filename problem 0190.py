'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given a circular array, compute its maximum subarray sum in O(n) time.

For example, given [8, -1, 3, 4], return 15 as we choose the numbers 3, 4, 
and 8 where the 8 is obtained from wrapping around.

Given [-4, 5, 1, 0], return 6 as we choose the numbers 5 and 1.
'''
List0 = [8,-1,3,4]
List = [-4,5,1,0]
List2 = [-5,3,4,5,-4,-6,-8,3,2,-10,2]
List3 = [-5,3,4,5,-4,-6,3,2,-10,2]
List4 = [-1,3,4,5,-4,-6,3,2,-10,2]
aaa= [-1,12,-2,12]
bbb=[12,-2,12,-1]

def new_list(List):
    lenn=len(List)
    new_L=[]
    compteur=0
    j=0
    while List[j]==0:
        j+=1
    sign=List[j]
    for i in range(j,lenn):
        if List[i]*sign>=0:
            compteur+=List[i]
        else:
            new_L.append(compteur)
            sign=List[i]
            compteur=List[i]
            
    new_L.append(compteur)
    if new_L[0]*new_L[-1]>0:
        new_L[0]+=new_L[-1]
        new_L=new_L[:-1]
    return new_L
              
        
def find_max_subbaray(List):
    print(List)
    new_L=new_list(List)       
    print(new_L)

    lenn=len(new_L)
    i=0
    while i<lenn:
        if i<0:
            i=0
        if new_L[i]<0:
            i+=1
        elif i<lenn-2:
            score1a=new_L[i]+new_L[i+1]
            score2a=new_L[i+2]+new_L[i+1]
            score1b=new_L[i]+new_L[i-1]
            score2b=new_L[i-2]+new_L[i-1]
            result1=0
            result2=0
            if score1a>0 and score2a>0:
                result1=new_L[i]+new_L[i+1]+new_L[i+2]
            if score2b>0 and score1b>0:
                result2=new_L[i]+new_L[i-1]+new_L[i-2]
                
            if result1==0 and result2==0:
                i+=1
            else:
                if result1>result2:
                    new_L[i]=result1
                    new_L=new_L[:i+1]+new_L[i+3:]
#                    lenn-=2
                else:
                    new_L[i]=result2
                    if i==0:
                        new_L=new_L[:-2]
                    elif i==1:
                        new_L=new_L[1:-1]
                    else:
                        new_L=new_L[:i-2]+new_L[i:]
                    i-=2
                lenn-=2
                
        else:
            i=lenn
                    
        
    print(new_L)   
        
        
    return max(new_L)
            
            
            

            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
        