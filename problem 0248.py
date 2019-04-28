'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Nvidia.

Find the maximum of two numbers without using any if-else statements, branching, or direct comparisons.
'''


# =============================================================================
# TRAVAIL SUR LES BITS (not my code)
# =============================================================================
def get_max(a,b):
    c=a-b
    k=(c>>31)&1
    return (a-k*c)

#on cherche a savoir si c est positif ou negatif (ligne du k)
# si c'est positif, k=0 pour avoir a -0*(a-b) = a
# si c'est negatif, k=1 pour avoir a -1*(a-b) = a-a+b = b