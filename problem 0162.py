'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Square.

Given a list of words, return the shortest unique prefix of each word. For example, given the list:

    dog
    cat
    apple
    apricot
    fish

Return the list:

    d
    c
    app
    apr
    f
'''

List=['dog','cat','apple','apricot','fish','dogy','arg']

def give_prefix(List):
    lenn=len(List)
    New_List=[]
    for i in range(lenn):
        number=0

        word = List[i]
        lenn_word=len(word)
        for j in range(lenn):
            if i==j:

                pass
            else:
                lenn_word2=len(List[j])
                nbr_check=min(lenn_word,lenn_word2)
                for k in range(nbr_check):
                    if word[k]!=List[j][k]:
                        if k>number:
                            number=k

                        break
                    elif k==nbr_check-1:
                        k=nbr_check
                        if k>number:
                            number=k
    
        New_List.append(word[:number+1])
        
    return New_List