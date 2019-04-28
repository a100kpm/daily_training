'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Lyft.

Given a list of integers and a number K, return which contiguous elements of the list sum to K.

For example, if the list is [1, 2, 3, 4, 5] and K is 9, then it should return [2, 3, 4].
'''


List = [1,2,3,4,5]

def contiguous_to_val(List,K):
    lenn=len(List)
    val=0
    Lister=[]
    for i in range(lenn):
        for j in range(i,lenn):
            val+=List[j]
            Lister.append(List[j])
            if val>K:
                val=0
                Lister=[]
                break
            if val==K:
                print(Lister)
                val=0
                Lister=[]
                return
#               break instead of return if you want all val
            
