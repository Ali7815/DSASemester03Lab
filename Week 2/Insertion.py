# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 13:09:39 2022

@author: Digital Zone
"""

import funcs
import time
randArray=funcs.RandomArray(30000)
startTime=time.time()
sortedArray=funcs.InsertionSort(randArray, 1,30000)
endTime=time.time()
totalTime=endTime-startTime
f=open(file="SortedInsertionSort.csv", mode="w")
for i in sortedArray:
    f.write(str(i) + "\n")