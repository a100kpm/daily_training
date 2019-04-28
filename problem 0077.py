'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Snapchat.

Given a list of possibly overlapping intervals, return a new list of intervals 
where all overlapping intervals have been merged.

The input list is not necessarily ordered in any way.

For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should return [(1, 3), (4, 10), (20, 25)].
'''

List = [(1, 3), (5, 8), (4, 10), (20, 25)]

def merge_list(List):
    stop = False
    
    i=0
    while stop==False:
        stop=True
        while i<len(List):
            start=List[i][0]
            end=List[i][1]
            j=0
            while j<len(List):
                if j==i:
                    j+=1
                
                else:
                    start_=List[j][0]
                    end_=List[j][1]
                    if (start<=start_ and end>=start_) or (start<=end_ and end>=end_):
                        List[j]=[]
                        new_min=min(start,start_)
                        new_max=max(end,end_)
                        List[i]=(new_min,new_max)
                        stop=False
                        List.remove([])
                        if i>j:
                            i-=1
                    else:
                        j+=1
            i+=1
            print(List)
    return List
        