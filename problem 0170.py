'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given a start word, an end word, and a dictionary of valid words, 
find the shortest transformation sequence from start to end such that only one 
letter is changed at each step of the sequence, and each transformed word exists 
in the dictionary. If there is no possible transformation, return null. 
Each word in the dictionary have the same length as start and end and is lowercase.

For example, given start = "dog", end = "cat", and dictionary = {"dot", "dop", "dat", "cat"}, 
return ["dog", "dot", "dat", "cat"].

Given start = "dog", end = "cat", and dictionary = 
{"dot", "tod", "dat", "dar"}, return null as there is no possible transformation from dog to cat.
'''

start = "dog"
end = "cat"
dictionnary1 = {"dot", "dop", "dat", "cat"}
dictionnary2 = {"dot", "tod", "dat", "dar"}

def find_shortest_word_path(start,end,dictionnary):
    if end not in dictionnary:
        return None
    List=[]
    List_temp=[start]
    for i in dictionnary:
        if i!=start:
            if distance_(i,start)==1:
                List_temp.append(i)
    List.append(List_temp)
    for i in dictionnary:
        List_temp=[i]
        for j in dictionnary:
            if i!=j:
                if distance_(i,j)==1:
                    List_temp.append(j)
        List.append(List_temp)
    
    lenn=len(List)
    List_distance=[[x[0],lenn] for x in List]
    List_word=[x[0] for x in List]
    List_distance[0][1]=0
    distance=0
    cont=True
    where=[start]
    while cont:
        distance+=1
        lenn2=len(where)
        new_where=[]
        for i in range(lenn2):
            pos_word=List_word.index(where[i])
            for j in range(1,len(List[pos_word])):
                word=List[pos_word][j]
                pos_temp=List_word.index(word)
                if List_distance[pos_temp][1]>distance:
                    List_distance[pos_temp][1]=distance
                    new_where.append(List_distance[pos_temp][0])
        where=new_where
        
        if len(where)==0 or distance==lenn:
            cont=False
            
    List_distance2=[[x[0],lenn] for x in List]
    where=[end]
    
    pos_end=List_word.index(end)
    
    List_distance2[pos_end][1]=0
    distance=0
    cont=True
    while cont:
        distance+=1
        lenn2=len(where)
        new_where=[]
        for i in range(lenn2):
            pos_word=List_word.index(where[i])
            for j in range(1,len(List[pos_word])):
                word=List[pos_word][j]
                pos_temp=List_word.index(word)
                if List_distance2[pos_temp][1]>distance:
                    List_distance2[pos_temp][1]=distance
                    new_where.append(List_distance2[pos_temp][0])
        where=new_where
        
        if len(where)==0 or distance==lenn:
            cont=False
            
    distance_final=List_distance[pos_end][1]
    result=['dog']
    distance=0
    for i in range(distance_final+1):
        distance+=1
        Last_word=result[-1]
        for j in range(lenn):
            if List_distance[j][1]==distance and List_distance2[j][1]==distance_final-distance:
                if distance_(Last_word,List_distance[j][0])==1:
                    result.append(List_distance[j][0])
                    break

        if len(result)==distance:
            if distance<=distance_final:
                return None
    return result
        
            
        
        
        
        
def distance_(word1,word2):
    lenn=len(word1)
    lenn2=len(word2)
    if lenn!=lenn2:
        return False
    compteur=0
    for i in range(lenn):
        if word1[i]!=word2[i]:
            compteur+=1
    if compteur==1:
        return True
    return False