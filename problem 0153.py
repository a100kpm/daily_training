'''
Good morning! Here's your coding interview problem for today.

Find an efficient algorithm to find the smallest distance (measured in number of words)
 between any two given words in a string.

For example, given words "hello", and "world" and a text content of 
"dog cat hello cat dog dog hello cat world", return 1 because there's only one word "cat" in between the two words.
'''

word1 ='hello'
word2 ='world'

text = 'dog cat hello cat dog dog hello cat world'


def smallest_distance_word(text,word1,word2):
    pos=None
    word=None
    distance=None
    a=text.split(' ')
    lenn=len(a)
    
    for i in range(lenn):
        if a[i]==word1 or a[i]==word2:
            if (a[i]==word1 and word==word2) or (a[i]==word2 and word==word1):
                n_dist=i-pos
                if distance:
                    if n_dist<distance:
                        distance=n_dist
                else:
                    distance=n_dist
            pos=i
            word=a[i]
            
    return distance-1