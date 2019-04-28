'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Nest.

Create a basic sentence checker that takes in a stream of characters and determines whether 
they form valid sentences. If a sentence is valid, the program should print it out.

We can consider a sentence valid if it conforms to the following rules:

    The sentence must start with a capital letter, followed by a lowercase letter or a space.
    All other characters must be lowercase letters, separators (,,;,:) or terminal marks (.,?,!,‽).
    There must be a single space between each word.
    The sentence must end with a terminal mark immediately following a word.
'''


sentence1= "Allo monsieur."
sentence2= "allo monsieur."
sentence3= "Allo monsieur"
sentence4= "ALlo monsieur."
sentence5= "Allo, monsieur."
sentence6= "Allo monsieur!"
sentence7= "Al??"
sentence8= "Al?o monsieur."
sentence9= "Allo  monsieur."

def valid_sent(sentence):
    start="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    other="abcdefghijklmnopqrstuvwxyz"
    separator=",;:"
    end="?!."
    
    if sentence[0] not in start:
        return False
    if sentence[-1] not in end:
        return False
    last=sentence[0]
    for i in sentence[1:-1]:
        if i ==" ":
            if last ==" ":
                return False
        elif i in separator and last in separator:
            return False
        elif i not in separator and i not in other:
            return False
        elif i in end:
            return False
        last=i
    
    return True


for i in range(1,10):
    a=f"sentence{i}"
    print(eval(a))
    print(valid_sent(eval(a)))
    
    
# eval marche ici, mais il faudrait plutôt faire une liste / un dictionnaire pour faire ce behaviour