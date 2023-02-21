# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 21:17:03 2022

@author: Digital Zone
"""

import funcs
randomArray=funcs.RandomArray(30000)
sortedArray=funcs.SelectionSort(randomArray, 0, 30000)
f=open(file="SortedSelectionSort.csv",mode="w")
for i in sortedArray:
    f.write(str(i) + "\n")