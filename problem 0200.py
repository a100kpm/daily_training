'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

Let X be a set of n intervals on the real line. We say that a set of points P "stabs"
 X if every interval in X contains at least one point in P. Compute the smallest set of points that stabs X.

For example, given the intervals [(1, 4), (4, 5), (7, 9), (9, 12)], you should return [4, 9].
'''

interval = [(1, 4), (4, 5), (7, 9), (9, 12)]
interval2= [(0,4),(3,5),(5,6),(7,9),(9,10)]

#suppose that interval are sorted by start position

def pinner(interval):
    result=[]
    pin=False
    lenn=len(interval)
    i=0
    while i < lenn:
        if pin==False:
            if i==lenn-1:
                result.append(interval[i][0])
            else:
                if interval[i+1][0]<=interval[i][1]:
                    pin=[interval[i+1][0],interval[i][1]]
                else:
                    result.append(interval[i][0])
            i+=1
                    
        else:
            if pin[1]>=interval[i][0]:
                pin[0]=interval[i][0]
                i+=1
            else:
                result.append(pin[0])
                pin=False
    if pin!=False:
        result.append(pin[0])
                
    return result