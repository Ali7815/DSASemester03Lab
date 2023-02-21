# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 13:07:05 2022

@author: Digital Zone
"""
#Random Number Generator
def RandomArray(size):
    import random
    randomArray=[]
    for i in range(size):
        num=random.randint(0,1000)
        randomArray.append(num)
    return randomArray
#Insertion Sort
def InsertionSort(array,start,end):
    for i in range(start+1,end):
        key=array[i]
        j=i-1
        while(key<array[j] and j>=0):
            array[j+1]=array[j]
            j=j-1
        array[j+1]=key
    return array
#Bubble Sort
def BubbleSort(array,start,end):
    i=end
    sorted=False
    while(i>1 and sorted==False):
        sorted=True
        for j in range (start+1,i):
            if(array[j-1]>array[j]):
                temp=array[j-1]
                array[j-1]=array[j]
                array[j]=temp
                sorted=False
        i=i-1
    return array
#MergeSort
def MergeSort(array,start,end):
    if(start<end):
        mid=(start+end)//2
        MergeSort(array, start, mid)
        MergeSort(array, mid+1, end)
        Merge(array,start,mid,end)
#Merge Sort
def Merge(array,p,q,r):
    n1=q-p+1
    n2=r-q
    L=[0]*(n1+1)
    R=[0]*(n2+1)
    for i in range(n1):
        L[i]=array[p+i]
    for j in range(n2):
        R[j]=array[q+j+1]
    if(type(array[0])==int):
        L[n1]=999999
        R[n2]=999999
    else:
        L[n1]="999999"
        R[n2]="999999"
    i=0
    j=0
    for k in range(p,r+1):
        if L[i]<R[j]:
            array[k]=L[i]
            i=i+1
        else:
            array[k]=R[j]
            j=j+1
#SelectionSort
def SelectionSort(array,start,end):
    for i in range(start,end):
        minIdx=i
        for j in range(i+1,end):
            if array[minIdx]>array[j]:
                minIdx=j
        temporary=array[i]
        array[i]=array[minIdx]
        array[minIdx]=temporary
    return array

           
#Insertion Sort for Hybrid Sort
def InsertionSort2(array):
    for i in range(1,len(array)):
        key=array[i]
        j=i-1
        while(key<array[j] and j>=0):
            array[j+1]=array[j]
            j=j-1
        array[j+1]=key
    
    return array

#Merge Sort for Hybrid Sort
def Merge2(array1,array2):
    i=0
    j=0
    newArray=[]
    while(i<len(array1) and j<len(array2)):
        if array1[i]<array2[j]:
            newArray.append(array1[i])
            i=i+1
        elif array2[j]<array1[i]:
            newArray.append(array2[j])
            j=j+1
        else:
            newArray.append(array1[i])
            newArray.append(array2[j])
            i=i+1
            j=j+1
    while(i<len(array1)):
        newArray.append(array1[i])
        i=i+1
    while(j<len(array2)):
        newArray.append(array2[j])
        j=j+1
    return newArray   
        

#Hybrid Merge Sort   
def HybridMergeSort(array,start,end):
    run=43
    for i in range(start,end,run):
        array[i:i+run]=InsertionSort2(array[i:i+run])
    newRun=run
    while newRun<end:
        for i in range(start,end,2*newRun):
            array[i:i+2*newRun]=Merge2(array[i:i+newRun], array[i+newRun:i+2*newRun])   
        newRun=2*newRun
    return array
        
#Shuffle Sort
def ShuffleArray(array,start,end):
    import random
    for i in range(start,end-1):
        idx=random.randint(start,end-1)
        temporary=array[i]
        array[i]=array[idx]
        array[idx]=temporary
    return array
        
 #Read Data          
def readData():
    f=open(file="Nvalues.txt",mode="r")
    lines=f.read()
    nValue=[]
    arr=lines.split()
    for s in arr:
        num=int(s)
        nValue.append(num)
    return nValue