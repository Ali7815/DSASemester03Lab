# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 17:45:10 2022

@author: Digital Zone
"""

import funcs
import time
f=open(file="words.txt",mode="r")
lines=f.read()
words=[]
arr=lines.split()
for i in arr:
    words.append(i)
startTime=time.time()
insertSort=funcs.InsertionSort(arr, 0, len(words))
endTime=time.time()
runTimeInsert=endTime-startTime
print("Insertion Sort Time : " , runTimeInsert)
startTime=time.time()
funcs.MergeSort(arr, 1, len(words)-1)
endTime=time.time()
runTimeMerge=endTime-startTime
print("Merge Sort Time : " , runTimeMerge)
randomArray=funcs.ShuffleArray(arr, 0, len(words))

startTime=time.time()
insertSort=funcs.InsertionSort(randomArray, 0, len(words))
endTimeins=time.time()
runTimeins=endTime-startTime
print("Insertion Sort Time After Shuffling : " , runTimeins)
startTime=time.time()
funcs.MergeSort(randomArray, 1, len(words)-1)
endTime=time.time()
runTimeMer=endTime-startTime
print("Merge Sort Time After Suffling: " , runTimeMer)
