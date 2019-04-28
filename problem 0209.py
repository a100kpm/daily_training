'''
Good morning! Here's your coding interview problem for today.

This problem was asked by YouTube.

Write a program that computes the length of the longest common subsequence of three 
given strings. For example, given "epidemiologist", "refrigeration", and "supercalifragilisticexpialodocious", 
it should return 5, since the longest common subsequence is "eieio".
'''

word = ["epi", "zapi", "pist"]



def longest_common(word):
    lenn=len(word)
    max_score = len(word[0])
    pos=0
    for i in range(1,lenn):
        if max_score>len(word[i]):
            max_score=len(word[i])
            pos=i
    word_min=word[pos]
    word=word[:i]+word[i+1:]
    lenn=lenn-1
    for j in range(max_score,0,-1):
        print('j=',j)
        for i in range(0,max_score-j+1):
            print('i=',i)
            current_sub_word=word_min[i:]
            print('sub_word=',current_sub_word)
            inside=True
            for k in range(lenn):
                print('k=',k,'work[k]=',word[k])
                if is_in_word(current_sub_word,word[k]):
                    pass
                else:
                    inside=False
            if inside==True:
                return j
    print('error?')
                
def is_in_word(current_sub_word,word):
    lenn=len(word)
    lenn2=len(current_sub_word)
    nbr_iter = lenn-lenn2+1
    for i in range(nbr_iter):
        if word[i:i+nbr_iter]==current_sub_word:
            return True
    return False

# version stupide:
word2 = ["epidemiologist", "refrigeration", "supercalifragilisticexpialodocious"]
word3 = ["eeppppiiii","eeeeppppiiii","epiepiepiepiepi"]
word4 = ["fabbbcccaa","fabbbcccaa","fbacac"]
def stupid_common(word):
    a=word[0]
    b=word[1]
    c=word[2]
    lenn1=len(a)
    lenn2=len(b)
    lenn3=len(c)
    if lenn1<=lenn2 and lenn1<=lenn3:
        min_word=a
        word1=b
        word2=c
    elif lenn2<=lenn1 and lenn2<=lenn3:
        min_word=b
        word1=a
        word2=c
    else:
        min_word=c
        word1=a
        word2=c
        
        
    max_sub_word,_=find_max_sub_word(min_word,word1,word2) 
    
    return len(max_sub_word)


def find_max_sub_word(min_word,word1,word2,subword=''):
    if len(min_word)==0:
        return subword,len(subword)
    
    letter=min_word[0]
    pos1=-1
    pos2=-1
    for i in range(len(word1)):
        if word1[i]==letter:
            pos1=i
            break
    for i in range(len(word2)):
        if word2[i]==letter:
            pos2=i
            break
            
    subword1,lenn1=find_max_sub_word(min_word[1:],word1,word2,subword)
    if (pos1+1)*(pos2+1)==0:
        return subword1,lenn1
    
    sub=subword+letter
    subword2,lenn2=find_max_sub_word(min_word[1:],word1[pos1+1:],word2[pos2+1:],sub)
    
    if lenn2>lenn1:
        return subword2,lenn2
    return subword1,lenn1
    

# =============================================================================
# =============================================================================
# # why ????
# =============================================================================
# =============================================================================

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def get_lcs(strings, context, indices):
    lcs_len = len(context)
    for letter in ALPHABET:
        new_indices = list()
        for j, string in enumerate(strings):
            index = string.find(letter, indices[j] + 1)
            if index == -1:
                break
            new_indices.append(index)
        if len(new_indices) == 3:
            length_cs = get_lcs(strings, context + letter, new_indices)
            if length_cs > lcs_len:
                lcs_len = length_cs

    return lcs_len


def get_lcs_helper(strings):
    return get_lcs(strings, "", [-1]*len(strings))


from timeit import default_timer as timer
start=timer()
print(stupid_common(word4))
end=timer()
print(end-start)

start=timer()

print(get_lcs_helper(word4))
end=timer()
print(end-start)
    
    
    