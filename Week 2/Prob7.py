# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 14:15:37 2022

@author: Digital Zone
"""
import numpy as np
import funcs
import time
nValue=funcs.readData()
a = [[None] * 5] * len(nValue)
tempo=[]
f=open(file="RunTime.csv",mode="w")
f.write("Value(n)" +"," + "Insertion Sort" +"," + "Merge Sort" +"," + "Hybrid Merge Sort" +"," + "Bubble Sort" +"," + "Slection Sort" + "\n")
for i in range(len(nValue)):
    n=nValue[i]
    array=funcs.RandomArray(n)
    insertStartTime=time.time()
    insert=funcs.InsertionSort(array, 0, n)
    insertEndTime=time.time()
    insert=insertEndTime-insertStartTime
    array=funcs.RandomArray(n)
    mergeStartTime=time.time()
    funcs.MergeSort(array, 0,n-1)
    mergeEndTime=time.time()
    merge=mergeEndTime-mergeStartTime
    array=funcs.RandomArray(n)
    hybridStartTime=time.time()
    hybrid=funcs.HybridMergeSort(array, 0, n)
    hybridEndTime=time.time()
    hybrid=hybridEndTime-hybridStartTime
    array=funcs.RandomArray(n)
    selectionStartTime=time.time()
    selection=funcs.SelectionSort(array, 0, n)
    selectioEndTime=time.time()
    selection=selectioEndTime-selectionStartTime
    array=funcs.RandomArray(n)
    bubbleStartTime=time.time()
    bubble=funcs.BubbleSort(array, 0, n)
    bubbleEndTime=time.time()
    bubble=bubbleEndTime-bubbleStartTime
    f.write(str(n) +"," +str(insert) +"," +str(merge) +"," +str(hybrid) +"," +str(bubble) +","+ str(selection) + "\n")
f.close()