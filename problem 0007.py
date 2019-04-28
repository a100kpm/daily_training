'''Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
'''


def nombre(List):
    if len(List)==0:
        return 1
    elif len(List)==1:
        return 1
    elif List[0]>2:
        return nombre(List[1:])
    elif List[0]==2 and List[1]>6:
        return nombre(List[1:])
    elif List[1]==0:
        return nombre(List[2:])
    else:
        return nombre(List[1:]) + nombre(List[2:])
    
    