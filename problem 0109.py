'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Cisco.

Given an unsigned 8-bit integer, swap its even and odd bits. 
The 1st and 2nd bit should be swapped, the 3rd and 4th bit should be swapped, and so on.

For example, 10101010 should be 01010101. 11100010 should be 11010001.

Bonus: Can you do this in one line?
'''

# bonus not made <_>


bit1 = '0b10101010'
bit2 = '0b11100010'

def swap_odd_even(bit,size=8):
    new_bit=''
    for i in range(1,5):
        new_bit+=bit[2*i+1]
        new_bit+=bit[2*i]
    return new_bit
