# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 14:50:36 2022

@author: Digital Zone
"""

def friendSlower(Input):
    A=Input
    con=1
    lis=[]
    row=1
    col=2
    for i in A:
        col=row+1
        for j in A[con:]:
            if(i[1]>=j[0]):
                lis.append(tuple([row,col]))
            col=col+1 
        con=con+1
        row=row+1
        col=0
    return lis
def friendsFaster(Input):
    print(Input)