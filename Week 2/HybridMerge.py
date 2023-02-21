# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 12:42:45 2022

@author: Digital Zone
"""

import funcs
randomArray=funcs.RandomArray(30000)
sortedArray=funcs.HybridMergeSort(randomArray, 0, 30000)
f=open(file="SortedHybridSort.csv",mode="w")
for i in sortedArray:
    f.write(str(i) + "\n")
