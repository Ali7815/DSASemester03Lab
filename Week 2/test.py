# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 14:24:14 2022

@author: Digital Zone
"""
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 14:54:29 2022

@author: Digital Zone
"""

import funcs
import time
n=10000
randomArray=funcs.RandomArray(n)
startTime=time.time()
sortedArray=funcs.HybridMergeSort(randomArray, 0, n)
endTime=time.time()
runTime=endTime-startTime
#print("Sorted Time : ", runTime)
#tempo.clear()
#col=0
#row=0
#n=nValue[i]
#print(n)
#randomArray=funcs.RandomArray(n)
#startTime=time.time()
#insertSort=funcs.InsertionSort(randomArray,0,n)
#endTime=time.time()
#runTime=endTime-startTime
#print(runTime)
#tempo.append(runTime)
#startTime=time.time()
#funcs.MergeSort(randomArray, 0, n-1)
#endTime=time.time()
#runTime=endTime-startTime
#print(runTime)
#tempo.append(runTime)
#startTime=time.time()
#hybridSort=funcs.HybridMergeSort(randomArray, 0, n)
#endTime=time.time()
#runTime=endTime-startTime
#print(runTime)
#tempo.append(runTime)
#startTime=time.time()
#mergeSort=funcs.SelectionSort(randomArray, 0, n)
#endTime=time.time()
#runTime=endTime-startTime
#print(runTime)
#tempo.append(runTime)
#startTime=time.time()
#mergeSort=funcs.BubbleSort(randomArray, 0, n)
#endTime=time.time()
#runTime=endTime-startTime
#print(runTime)
#tempo.append(runTime)
#print("row", tempo)
#a[row].append(tempo)
#row=row+1
