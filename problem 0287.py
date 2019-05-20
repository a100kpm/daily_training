'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Quora.

You are given a list of (website, user) pairs that represent users visiting websites. 
Come up with a program that identifies the top k pairs of websites with the greatest similarity.

For example, suppose k = 1, and the list of tuples is:

[('a', 1), ('a', 3), ('a', 5),
 ('b', 2), ('b', 6),
 ('c', 1), ('c', 2), ('c', 3), ('c', 4), ('c', 5)
 ('d', 4), ('d', 5), ('d', 6), ('d', 7),
 ('e', 1), ('e', 3), ('e': 5), ('e', 6)]

Then a reasonable similarity metric would most likely conclude that a and e are 
the most similar, so your program should return [('a', 'e')].
'''

k=1
tup=[('a', 1), ('a', 3), ('a', 5), 
     ('b', 2), ('b', 6),
     ('c', 1), ('c', 2), ('c', 3), ('c', 4), ('c', 5),
     ('d', 4), ('d', 5), ('d', 6), ('d', 7),
     ('e', 1), ('e', 3), ('e', 5), ('e', 6)]

def find_k_closest(k,tup):
#    we suppose k isn't too big and k>0
    List=[]

    for i in tup:
        if i[0] not in List:
            List.append(i[0])
    List_size=[0]*len(List)
    for i in tup:
        lettre=i[0]
        pos=List.index(lettre)
        List_size[pos]+=1
    max_size=max(List_size)
    factor=1
    while max_size>9:
        max_size/=10
        factor+=1
            
    lenn=len(List)-1
    rez=[]
    for i in range(lenn):

        letter1=List[i]
        list_chiffre=[]
        for chiffre in tup:
            if chiffre[0] == letter1:
                list_chiffre.append(chiffre[1])
        for j in range(i+1,lenn+1):
            letter2=List[j]
            list_temp_chiffre=[]
            for chiffre in tup:
                if chiffre[0]==letter2:
                    list_temp_chiffre.append(chiffre[1])
            nbr=0
            for chiffre in list_temp_chiffre:
                if chiffre in list_chiffre:
                    nbr+=1
            rez.append((letter1,letter2,nbr-0.1**factor*abs(List_size[i]-List_size[j])))
            
    list_val=[]
    list_rez=[]
    lenn=len(rez)
    for i in rez:
        if i[2] not in list_val:
            list_val.append(i[2])
    list_val.sort(reverse=True)  
    i=0 
    j=0    
    while k>0:
        if rez[i][2]==list_val[j]:
            list_rez.append((rez[i][0],rez[i][1]))
            k-=1
        i+=1
        if i==lenn:
            i=0
            j+=1
            
    return list_rez
    