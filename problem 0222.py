'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Quora.

Given an absolute pathname that may have . or .. as part of it, return the shortest standardized path.

For example, given "/usr/bin/../bin/./scripts/../", return "/usr/bin/".
'''


path = "/usr/bin/../bin/./scripts/../"
# "." = stay where you are
# "..# = go back one directory

def standard_path(path):
    ssplit=path.split("/")
    result=[]
    for elem in ssplit:
        print('elem=',elem)
        
        if elem=='.':
            pass
        elif elem=='..':
            result=result[:-1]
        else:
            result.append(elem+'/')
        print(result)    
    result = ''.join(result)
    return result[:-1]
        

