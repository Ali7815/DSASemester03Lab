# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 21:50:00 2022

@author: Digital Zone
"""
import funcs
Array=[3,4,7,8,0,1,23,-2,-5]
StartingIndex=input("Enter Starting Index : ")
EndingIndex=input("Enter Ending Index : ")
StartingIndex=int(StartingIndex)
EndingIndex=int(EndingIndex)
index=funcs.Minimum(Array, StartingIndex, EndingIndex)
print(index)