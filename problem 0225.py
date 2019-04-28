'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Bloomberg.

There are N prisoners standing in a circle, waiting to be executed. 
The executions are carried out starting with the kth person, and removing every 
successive kth person going clockwise until there is no one left.

Given N and k, write an algorithm to determine where a prisoner should stand in order to be the last survivor.

For example, if N = 5 and k = 2, the order of executions would be [2, 4, 1, 5, 3], so you should return 3.

Bonus: Find an O(log N) solution if k = 2.
'''

N=5
k=2

def easy_kill_order(N,k):
    List=[]
    for i in range(1,N+1):
        List.append(i)
        
    murder=[]
    pos=k-1
    
    while True:
#        print('murder=',murder)
#        print('List=',List)
#        print(pos)
#        input()
        murder.append(List[pos])
        List=List[:pos]+List[pos+1:]
        
        new_pos=pos+k-1
        if len(List)==0:
            return murder
        while new_pos>=len(List):
#            print('new_pos=',new_pos)
#            print('len=',len(List))
#            input()
            new_pos=new_pos-len(List)
        
        pos=new_pos
        

def log_kill_order(N):
#    k=2

    if power_of_two(N)==True:
        return 1
    
    pos=1
    
    List=[]
    for i in range(1,N+1):
        List.append(i)
        
    while True:
        List=List[:pos]+List[pos+1:]
        pos=pos+1
        print('len(List)=',len(List))
        print(pos)
        print('List=',List)
        input()

    
        if pos>=len(List):
            pos=pos-len(List)
            
        if power_of_two(len(List))==True:
            return List[pos-1]


def power_of_two(N):
    if N==1 or N==2:
        return True
    val = bin(N)
    for i in range(3,len(val)):
        if val[i]=='1':
            return False
    return True

def better_power_of_two(N):
    if N<=0:
        return False
    
    return n & (n-1)==0