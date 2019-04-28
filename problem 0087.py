'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Uber.

A rule looks like this:

A NE B

This means this means point A is located northeast of point B.

A SW C

means that point A is southwest of C.

Given a list of rules, check if the sum of the rules validate. For example:

A N B
B NE C
C N A

does not validate, since A cannot be both north and south of C.

A NW B
A N B

is considered valid.
'''

List=[]
List.append('A N B')
List.append('B NE C')
List.append('C N A')

List1=[]
List1.append('A NW B')
List1.append('A N B')

def logic(List):
    Listing=[]
    for i in range(len(List)):
        if [List[i][0],[[],[]],[[],[]] ] not in Listing:
            Listing.append([List[i][0],[[],[]],[[],[]] ])
        if [List[i][-1],[[],[]],[[],[]] ] not in Listing:
            Listing.append([List[i][-1],[[],[]],[[],[]] ])
#   N/S into W/E
    Lister=[]
    for i in range(len(Listing)):
        Lister.append(Listing[i][0])
        
    for i in range(len(List)):
        val1 = List[i].split(' ')[0]
        index1  = Lister.index(val1)
        val2 = List[i].split(' ')[2]
        index2 = Lister.index(val2)
        travail=List[i].split(' ')[1]
    
        for j in range(len(travail)):
            if travail[j]=='N':
                Listing[index1][1][0]+=val2
                Listing[index2][1][1]+=val1
            if travail[j]=='S':
                Listing[index1][1][1]+=val2
                Listing[index2][1][0]+=val1
            if travail[j]=='W':
                Listing[index1][2][0]+=val2
                Listing[index2][2][1]+=val1
            if travail[j]=='E':
                Listing[index1][2][1]+=val2
                Listing[index2][2][0]+=val1 
                
    for i in range(len(Listing)):
        
        N=Listing[i][1][1]
        S=Listing[i][1][0]
        W=Listing[i][2][1]
        E=Listing[i][2][0]


# a finir (sommer les éléments)
    