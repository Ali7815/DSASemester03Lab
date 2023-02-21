# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 19:11:44 2022

@author: Digital Zone
"""

import funcs
import time
randomArray=funcs.RandomArray(30000)
startTime=time.time()
funcs.MergeSort(randomArray, 0, 30000-1)
endTime=time.time()
runTime=endTime-startTime
print("Sorted Time : ", runTime)
f=open(file="SortedMergeSort.csv", mode="w")
for i in randomArray:
    f.write(str(i) + "\n")
