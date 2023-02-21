# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 14:54:29 2022

@author: Digital Zone
"""

import funcs
import time
n=30000
randArray=funcs.RandomArray(n)

bubbleSort=funcs.BubbleSort(randArray, 0, n)
f=open(file="SortedBubbleSort.csv", mode="w")
for i in bubbleSort:
    f.write(str(i) + "\n")