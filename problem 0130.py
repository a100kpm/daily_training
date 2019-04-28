'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given an array of numbers representing the stock prices of a company in chronological 
order and an integer k, return the maximum profit you can make from k buys and sells. 
You must buy the stock before you can sell it, and you must sell the stock before you can buy it again.

For example, given k = 2 and the array [5, 2, 4, 0, 1], you should return 3.
'''

array = [5,2,4,0,1,3,4]
k=2


def max_profit(array,k):
    if k==1:
        profit_m=0
        for i in range(1,len(array)-1):
            profit=array[i]*-1+max(array[i+1:])
            if profit>profit_m:
                profit_m = profit
        return profit_m
    
    start=2*(k-1)
    profit_max=0
    for i in range(start,len(array)-1):
        print(i)
        profit_droit= -1*array[i] + max(array[i+1:])
        profit_gauche = max_profit(array[:i],k-1)
        profit=profit_droit+profit_gauche
        print('profit_droit=',profit_droit)
        print('profit_gauche=',profit_gauche)
        if profit>profit_max:
            profit_max=profit
    
    return profit_max