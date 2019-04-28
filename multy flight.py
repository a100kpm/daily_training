# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 16:07:02 2018

@author: iannis
"""


List_fly=[['HNL','AKL'],['YUL','ORD'],['ORD','SFO'],['SFO','HNL']]
List_fly2=[[1,2],[2,3],[1,3],[3,1],[3,1],[2,3],[1,2]]
Current_list=[]


def multy_flight(List_fly,start,Current_list):
    lenn=len(List_fly)
    
    result=False
    for i in range(lenn):
        if List_fly[i][0]==start:
            new_list=List_fly[:]
            Current_list.append(new_list.pop(i))
            result,fly_listing=multy_flight(new_list,Current_list[-1][1],Current_list)
        if result==True:
            break
        
    
    fly_listing=Current_list
    if len(List_fly)==0:
        result=True
    
        
    return result,fly_listing
    
def fly_cleaning(fly_listing):
    lenn=len(fly_listing)-2
    for i in range(lenn):
        if fly_listing[i][1]!=fly_listing[i+1][0]:
            del fly_listing[i+1]
    return fly_listing              
            
def multiple_flight(List_fly,start):
    Current_list=[]
    result,fly_listing= multy_flight(List_fly,start,Current_list)
    if result==True:
        fly_result=fly_cleaning(fly_listing)
        return result,fly_result
    return result,[]
    
    
    
        