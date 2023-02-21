# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 12:48:52 2022

@author: Digital Zone
"""

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