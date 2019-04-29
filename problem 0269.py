'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

You are given an string representing the initial conditions of some dominoes. Each element can take one of three values:

    L, meaning the domino has just been pushed to the left,
    R, meaning the domino has just been pushed to the right, or
    ., meaning the domino is standing still.

Determine the orientation of each tile when the dominoes stop falling. Note that if a domino receives a force from the left and right side simultaneously, it will remain upright.

For example, given the string .L.R....L, you should return LL.RRRLLL.

Given the string ..R...L.L, you should return ..RR.LLLL.
'''

string = "..R...L.L"


def domino_push(string):
    string2=string
    

        
    lenn=len(string)-1
    changement=True
    while changement==True:
        changement=False
        if string[0]=='.' and string[1]=='L':
            string2=='L'+string2[1:]
            changement=True
        if string[-1]=='.' and string[-2]=='R':
            string2[-1]=string2[:-1]+'R'
            changement=True
        for i in range(1,lenn):
            if string[i]=='.':
                if string[i-1] == 'R' and string[i+1]== 'L':
                    pass
                elif string[i-1] == 'R':
                    string2=string2[:i]+'R'+string2[i+1:]
                    changement=True
                elif string[i+1] == 'L':
                    string2=string2[:i]+'L'+string2[i+1:]
                    changement=True
        
        string=string2
        print(string)
        input()
        
    return string
        