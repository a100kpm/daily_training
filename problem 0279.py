'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Twitter.

A classroom consists of N students, whose friendships can be represented in an adjacency list. 
For example, the following descibes a situation where 0 is friends with 1 and 2, 3 is friends with 6, and so on.

{0: [1, 2],
 1: [0, 5],
 2: [0],
 3: [6],
 4: [],
 5: [1],
 6: [3]} 

Each student can be placed in a friend group, which can be defined as the transitive 
closure of that student's friendship relations. In other words, this is the smallest 
set such that no student in the group has any friends outside this group. For the example above, 
the friend groups would be {0, 1, 2, 5}, {3, 6}, {4}.

Given a friendship list such as the one above, determine the number of friend groups in the class.
'''

dictionnaire = {0: [1, 2],
 1: [0, 5],
 2: [0],
 3: [6],
 4: [],
 5: [1],
 6: [3]} 


def regroup_friend(dictionnaire):
    
    List_groupe=[]
    
    while len(dictionnaire)>0:
        changement=True
        start=True
        while changement==True:
            changement=False
            list_del=[]
            for i in dictionnaire:
                
                if start==True:
                    new_dict=set()
                    new_dict.add(i)
                    for j in dictionnaire[i]:
                        new_dict.add(j)
                    list_del.append(i)
                    start=False
                    changement=True
                else:
                    if i in new_dict:
                        new_dict.add(i)
                        for j in dictionnaire[i]:
                            new_dict.add(j)
                        if i not in list_del:
                            list_del.append(i)
                        changement=True
                    for j in dictionnaire[i]:
                        if j in new_dict:
                            changement=True
                            new_dict.add(i)
                            for k in dictionnaire[i]:
                                new_dict.add(k)
                            if i not in list_del:
                                list_del.append(i)
                            break
                        
            for i in list_del:
                del(dictionnaire[i])
        List_groupe.append(new_dict)

            
    return List_groupe
                        
    
    