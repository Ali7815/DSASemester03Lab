# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 12:47:52 2022

@author: Digital Zone
"""

import funcs
import time
import random
import matplotlib.pyplot as p
import pandas as pd


    
def Prob1():
    n=10
    timeTaken=[]
    nValue=[]
    f=open(file="Time.csv",mode="w")
    f.write("N,Time" + "\n")
    while n<=500:
        A=[]
        for i in range(0,n):
            num=random.randint(0, 100)
            A.append(num)
        startTime=time.time()
        # print("UnSorted A:",A)
        funcs.QuickSort(A, 0, len(A)-1)
        endTime=time.time()
        # print(endTime-startTime)
        timeTaken.append(endTime-startTime)
        nValue.append(n)
        # print("Sorted Array",A)
        n+=1
    for i in range(0,len(nValue)):
        print(nValue[i],timeTaken[i])
        f.write(str(nValue[i]) + "," + str(timeTaken[i]) + "\n")
        
    p.plot(nValue,timeTaken)
    p.show()
def QuickSort(A,low,high):
    if low<high:
        pi=partition(A,low,high)
        QuickSort(A,low,pi-1)
        QuickSort(A,pi+1,high)


def partition(A,low,high):
    pivot=A[high]
    i=low-1
    for j in range(low,high):
        if A[j]<=pivot:
            i=i+1
            temp=A[j]
            A[j]=A[i]
            A[i]=temp
    temp=A[i+1]
    A[i+1]=A[high]
    A[high]=temp
    return i+1
def main():
    Prob1()
if __name__=="__main__":
    main()