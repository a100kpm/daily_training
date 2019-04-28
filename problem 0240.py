'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Spotify.

There are N couples sitting in a row of length 2 * N. They are currently ordered randomly, but would like to rearrange themselves so that each couple's partners can sit side by side.

What is the minimum number of swaps necessary for this to happen?
'''

# entre 0 et N-1
# le problème est équivalent a un tri pour lequel on sait à l'avance où 
# l'on doit envoyer les valeurs qui ne sont pas bien placée
#
# between 0 and N-1 
# the problem is the same as a sort for which we know where to
# send every value who aren't well placed