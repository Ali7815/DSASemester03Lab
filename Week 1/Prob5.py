# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 10:43:43 2022

@author: Digital Zone
"""
import funcs
str="University of Engineering and Technology Lahore"
starting=input("Enter Starting Index : ")
ending=input("Enter Ending Index : ")
starting=int(starting)
ending=int(ending)
res=funcs.StringReverse(str, starting, ending)
print(res)